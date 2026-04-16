import requests
import sys
from datetime import datetime

class AuraFitAPITester:
    def __init__(self, base_url="https://instant-style-2.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0

    def run_test(self, name, method, endpoint, expected_status, data=None, params=None):
        """Run a single API test"""
        url = f"{self.api_url}/{endpoint}" if endpoint else f"{self.api_url}/"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    response_data = response.json()
                    print(f"   Response: {response_data}")
                    return True, response_data
                except:
                    return True, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    error_data = response.json()
                    print(f"   Error: {error_data}")
                except:
                    print(f"   Error: {response.text}")
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_root_endpoint(self):
        """Test GET /api/ returns AuraFit message"""
        success, response = self.run_test(
            "Root Endpoint",
            "GET",
            "",
            200
        )
        if success and 'message' in response:
            if 'AuraFit' in response['message']:
                print("   ✅ AuraFit message found")
                return True
            else:
                print("   ❌ AuraFit message not found in response")
                return False
        return False

    def test_stats_endpoint(self):
        """Test GET /api/stats returns total_outfits and by_occasion data"""
        success, response = self.run_test(
            "Stats Endpoint",
            "GET",
            "stats",
            200
        )
        if success:
            if 'total_outfits' in response and 'by_occasion' in response:
                print(f"   ✅ Total outfits: {response['total_outfits']}")
                print(f"   ✅ By occasion: {response['by_occasion']}")
                return True
            else:
                print("   ❌ Missing total_outfits or by_occasion in response")
                return False
        return False

    def test_outfits_endpoint(self):
        """Test GET /api/outfits with various filters"""
        # Test basic outfits endpoint
        success, response = self.run_test(
            "Outfits Endpoint (Basic)",
            "GET",
            "outfits",
            200
        )
        if not success:
            return False
        
        if 'outfits' not in response or 'count' not in response:
            print("   ❌ Missing outfits or count in response")
            return False
        
        print(f"   ✅ Found {response['count']} outfits")
        
        # Test with filters
        filters_to_test = [
            {"occasion": "college", "gender": "men"},
            {"occasion": "casual", "gender": "women"},
            {"season": "summer", "limit": 2},
            {"style": "formal", "limit": 1},
            {"occasion": "party", "gender": "women", "season": "all", "style": "elegant"}
        ]
        
        for i, filter_params in enumerate(filters_to_test):
            success, response = self.run_test(
                f"Outfits with Filters {i+1}",
                "GET",
                "outfits",
                200,
                params=filter_params
            )
            if success:
                print(f"   ✅ Filter {filter_params} returned {response.get('count', 0)} outfits")
            else:
                return False
        
        return True

    def test_outfit_detail_endpoint(self):
        """Test GET /api/outfits/{id} returns single outfit detail"""
        # First get an outfit ID
        success, response = self.run_test(
            "Get Outfit for Detail Test",
            "GET",
            "outfits",
            200,
            params={"limit": 1}
        )
        
        if not success or not response.get('outfits'):
            print("   ❌ Could not get outfit for detail test")
            return False
        
        outfit_id = response['outfits'][0]['id']
        
        # Test outfit detail
        success, response = self.run_test(
            "Outfit Detail Endpoint",
            "GET",
            f"outfits/{outfit_id}",
            200
        )
        
        if success:
            required_fields = ['id', 'title', 'description', 'occasion', 'gender', 'season', 'style', 'image_url', 'items']
            missing_fields = [field for field in required_fields if field not in response]
            if missing_fields:
                print(f"   ❌ Missing fields: {missing_fields}")
                return False
            else:
                print(f"   ✅ Outfit detail complete for: {response['title']}")
                return True
        return False

    def test_filters_endpoint(self):
        """Test GET /api/filters returns available filter options"""
        success, response = self.run_test(
            "Filters Endpoint",
            "GET",
            "filters",
            200
        )
        
        if success:
            required_fields = ['occasions', 'genders', 'seasons', 'styles']
            missing_fields = [field for field in required_fields if field not in response]
            if missing_fields:
                print(f"   ❌ Missing filter fields: {missing_fields}")
                return False
            else:
                print(f"   ✅ Available occasions: {response['occasions']}")
                print(f"   ✅ Available genders: {response['genders']}")
                print(f"   ✅ Available seasons: {response['seasons']}")
                print(f"   ✅ Available styles: {response['styles']}")
                return True
        return False

    def test_database_seeding(self):
        """Test that database has 23 outfits seeded"""
        success, response = self.run_test(
            "Database Seeding Check",
            "GET",
            "stats",
            200
        )
        
        if success and 'total_outfits' in response:
            total_outfits = response['total_outfits']
            if total_outfits == 23:
                print(f"   ✅ Database correctly seeded with {total_outfits} outfits")
                return True
            else:
                print(f"   ❌ Expected 23 outfits, found {total_outfits}")
                return False
        return False

def main():
    print("🚀 Starting AuraFit Backend API Tests")
    print("=" * 50)
    
    tester = AuraFitAPITester()
    
    # Run all tests
    tests = [
        tester.test_root_endpoint,
        tester.test_stats_endpoint,
        tester.test_database_seeding,
        tester.test_filters_endpoint,
        tester.test_outfits_endpoint,
        tester.test_outfit_detail_endpoint,
    ]
    
    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"❌ Test failed with exception: {str(e)}")
    
    # Print results
    print("\n" + "=" * 50)
    print(f"📊 Tests passed: {tester.tests_passed}/{tester.tests_run}")
    
    if tester.tests_passed == tester.tests_run:
        print("🎉 All backend tests passed!")
        return 0
    else:
        print("⚠️  Some backend tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())