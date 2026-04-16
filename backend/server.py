from fastapi import FastAPI, APIRouter, Query
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
# from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
import uuid
from datetime import datetime, timezone

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# mongo_url = os.environ['MONGO_URL']
# client = AsyncIOMotorClient(mongo_url)
# db = client[os.environ['DB_NAME']]

app = FastAPI()
api_router = APIRouter(prefix="/api")

# Models
class ClothingItem(BaseModel):
    name: str
    category: str
    color: str
    description: str

class Outfit(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    occasion: str
    gender: str
    season: str
    style: str
    image_url: str
    items: List[ClothingItem]
    tags: List[str]
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class OutfitFilters(BaseModel):
    occasions: List[str]
    genders: List[str]
    seasons: List[str]
    styles: List[str]

# Seed Data
SEED_OUTFITS = [
    # MEN - COLLEGE
    {
        "title": "Campus Cool",
        "description": "A relaxed yet put-together look perfect for lectures and campus hangouts. The layered approach gives you flexibility throughout the day.",
        "occasion": "college",
        "gender": "men",
        "season": "all",
        "style": "casual",
        "image_url": "https://images.unsplash.com/photo-1770739886778-ab36c4b55dbd?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2OTV8MHwxfHNlYXJjaHwxfHxjYXN1YWwlMjBjb2xsZWdlJTIwc3R1ZGVudCUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY2OTB8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Oversized Graphic Tee", "category": "top", "color": "White", "description": "Relaxed fit cotton tee with minimal print"},
            {"name": "Straight Fit Chinos", "category": "bottom", "color": "Khaki", "description": "Comfortable cotton chinos"},
            {"name": "White Sneakers", "category": "shoes", "color": "White", "description": "Clean low-top canvas sneakers"},
            {"name": "Canvas Backpack", "category": "accessories", "color": "Navy", "description": "Simple structured backpack"}
        ],
        "tags": ["comfortable", "layered", "campus", "everyday"]
    },
    {
        "title": "Study Session Ready",
        "description": "Effortless smart-casual that works from morning class to evening study group. Clean lines with a touch of personality.",
        "occasion": "college",
        "gender": "men",
        "season": "fall",
        "style": "casual",
        "image_url": "https://images.unsplash.com/photo-1682527894541-45dc10e7cc66?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2OTV8MHwxfHNlYXJjaHwzfHxjYXN1YWwlMjBjb2xsZWdlJTIwc3R1ZGVudCUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY2OTB8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Crew Neck Sweater", "category": "top", "color": "Charcoal", "description": "Wool-blend crew neck sweater"},
            {"name": "Slim Fit Jeans", "category": "bottom", "color": "Dark Wash", "description": "Classic dark wash denim"},
            {"name": "Leather Boots", "category": "shoes", "color": "Brown", "description": "Chelsea boots with rubber sole"},
            {"name": "Minimalist Watch", "category": "accessories", "color": "Silver", "description": "Clean dial analog watch"}
        ],
        "tags": ["smart-casual", "fall", "layered", "campus"]
    },
    # MEN - CASUAL
    {
        "title": "Weekend Wanderer",
        "description": "The perfect weekend outfit that balances comfort and style. Great for brunch, errands, or a casual day out with friends.",
        "occasion": "casual",
        "gender": "men",
        "season": "summer",
        "style": "casual",
        "image_url": "https://images.unsplash.com/photo-1775306413232-fecd45367613?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHw0fHxtZW5zJTIwY2FzdWFsJTIwc3VtbWVyJTIwb3V0Zml0fGVufDB8fHx8MTc3NjM0NjgwMXww&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Polo Shirt", "category": "top", "color": "Light Blue", "description": "Classic fit pique polo"},
            {"name": "Slim Fit Jeans", "category": "bottom", "color": "Black", "description": "Tapered black denim"},
            {"name": "White Sneakers", "category": "shoes", "color": "White", "description": "Leather low-top sneakers"},
            {"name": "Leather Belt", "category": "accessories", "color": "Brown", "description": "Simple leather belt"}
        ],
        "tags": ["weekend", "relaxed", "summer", "clean"]
    },
    {
        "title": "Summer Vibes",
        "description": "Bold and expressive summer look. The printed shirt adds personality while keeping things breezy and comfortable for warm days.",
        "occasion": "casual",
        "gender": "men",
        "season": "summer",
        "style": "streetwear",
        "image_url": "https://images.unsplash.com/photo-1765206151637-49acefb1a4a5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwyfHxtZW5zJTIwY2FzdWFsJTIwc3VtbWVyJTIwb3V0Zml0fGVufDB8fHx8MTc3NjM0NjgwMXww&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Printed Camp Collar Shirt", "category": "top", "color": "Orange Floral", "description": "Relaxed fit camp collar with tropical print"},
            {"name": "Chino Shorts", "category": "bottom", "color": "White", "description": "Tailored cotton shorts above the knee"},
            {"name": "Loafers", "category": "shoes", "color": "Tan", "description": "Suede penny loafers"},
            {"name": "Statement Watch", "category": "accessories", "color": "Rose Gold", "description": "Chunky dial dress watch"}
        ],
        "tags": ["summer", "bold", "printed", "tropical"]
    },
    # MEN - STREETWEAR
    {
        "title": "Urban Edge",
        "description": "Street-smart with an attitude. This look combines oversized silhouettes with bold layering for a fashion-forward urban vibe.",
        "occasion": "casual",
        "gender": "men",
        "season": "all",
        "style": "streetwear",
        "image_url": "https://images.unsplash.com/photo-1586897414933-79708324005e?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDN8MHwxfHNlYXJjaHwxfHxtZW5zJTIwc3RyZWV0d2VhciUyMG91dGZpdCUyMGZhc2hpb258ZW58MHx8fHwxNzc2MzQ2NjkwfDA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Oversized Hoodie", "category": "top", "color": "Black", "description": "Heavyweight cotton hoodie with dropped shoulders"},
            {"name": "Cargo Pants", "category": "bottom", "color": "Olive", "description": "Wide-leg cargo with utility pockets"},
            {"name": "High-Top Sneakers", "category": "shoes", "color": "White/Black", "description": "Chunky platform high-tops"},
            {"name": "Crossbody Bag", "category": "accessories", "color": "Black", "description": "Nylon chest bag"}
        ],
        "tags": ["streetwear", "urban", "oversized", "layered"]
    },
    # MEN - FORMAL
    {
        "title": "Power Player",
        "description": "Command the room with this sharp, modern suit ensemble. Double-breasted styling adds authority while maintaining a sleek silhouette.",
        "occasion": "formal",
        "gender": "men",
        "season": "all",
        "style": "formal",
        "image_url": "https://images.unsplash.com/photo-1768696082783-4313d98341ae?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwzfHxtZW5zJTIwZm9ybWFsJTIwb3V0Zml0JTIwZmFzaGlvbnxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Double-Breasted Blazer", "category": "top", "color": "Black", "description": "Slim fit double-breasted wool blazer"},
            {"name": "Tailored Trousers", "category": "bottom", "color": "Black", "description": "High-waisted pleated trousers"},
            {"name": "Oxford Shoes", "category": "shoes", "color": "Black", "description": "Polished leather cap-toe oxfords"},
            {"name": "Silk Tie", "category": "accessories", "color": "Charcoal", "description": "Slim silk tie with subtle texture"}
        ],
        "tags": ["formal", "power", "sharp", "professional"]
    },
    {
        "title": "Modern Executive",
        "description": "Contemporary business look that blends tradition with modern cuts. The turtleneck under blazer combo keeps it fresh and sophisticated.",
        "occasion": "formal",
        "gender": "men",
        "season": "winter",
        "style": "formal",
        "image_url": "https://images.unsplash.com/photo-1640651663715-a1ee960c8690?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwxfHxtZW5zJTIwZm9ybWFsJTIwb3V0Zml0JTIwZmFzaGlvbnxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Slim Fit Blazer", "category": "top", "color": "Black", "description": "Single-breasted wool-blend blazer"},
            {"name": "Turtleneck", "category": "top", "color": "White", "description": "Fine knit merino turtleneck"},
            {"name": "Tailored Trousers", "category": "bottom", "color": "Black", "description": "Tapered wool trousers"},
            {"name": "Chelsea Boots", "category": "shoes", "color": "Black", "description": "Sleek leather Chelsea boots"}
        ],
        "tags": ["executive", "modern", "turtleneck", "winter"]
    },
    # MEN - DATE
    {
        "title": "Date Night Charm",
        "description": "Effortlessly suave. The textured blazer adds personality while the black turtleneck keeps things sleek and mysterious.",
        "occasion": "date",
        "gender": "men",
        "season": "all",
        "style": "elegant",
        "image_url": "https://images.unsplash.com/photo-1741709846033-67a45021fcb2?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwyfHxtZW5zJTIwcGFydHklMjBuaWdodCUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Textured Blazer", "category": "top", "color": "Silver/Grey", "description": "Embroidered slim-fit evening blazer"},
            {"name": "Turtleneck", "category": "top", "color": "Black", "description": "Slim fit mock neck in fine knit"},
            {"name": "Slim Trousers", "category": "bottom", "color": "Charcoal", "description": "Tapered fit dress trousers"},
            {"name": "Dress Shoes", "category": "shoes", "color": "Black", "description": "Patent leather slip-ons"},
            {"name": "Aviator Sunglasses", "category": "accessories", "color": "Gold", "description": "Classic metal frame aviators"}
        ],
        "tags": ["date", "evening", "suave", "textured"]
    },
    {
        "title": "Classic Gentleman",
        "description": "Timeless and confident. The bow tie and suspenders combo adds personality without trying too hard. Perfect for upscale dining.",
        "occasion": "date",
        "gender": "men",
        "season": "all",
        "style": "elegant",
        "image_url": "https://images.unsplash.com/photo-1680349434914-f87812a15180?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwxfHxtZW5zJTIwcGFydHklMjBuaWdodCUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Crisp White Shirt", "category": "top", "color": "White", "description": "Slim fit cotton dress shirt"},
            {"name": "Dress Trousers", "category": "bottom", "color": "Black", "description": "High-waisted pleated trousers"},
            {"name": "Suspenders", "category": "accessories", "color": "Navy", "description": "Clip-on Y-back suspenders"},
            {"name": "Bow Tie", "category": "accessories", "color": "Black", "description": "Satin self-tie bow tie"},
            {"name": "Oxford Shoes", "category": "shoes", "color": "Black", "description": "Classic leather oxfords"}
        ],
        "tags": ["gentleman", "classic", "bow-tie", "suspenders"]
    },
    # MEN - WEDDING
    {
        "title": "Wedding Guest Sharp",
        "description": "Stand out at any wedding without upstaging the groom. This tailored look strikes the perfect balance between festive and refined.",
        "occasion": "wedding",
        "gender": "men",
        "season": "all",
        "style": "formal",
        "image_url": "https://images.unsplash.com/photo-1646176724600-f4d40046feed?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHw0fHxtZW5zJTIwcGFydHklMjBuaWdodCUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Three-Piece Suit", "category": "top", "color": "Black", "description": "Slim fit wool three-piece with vest"},
            {"name": "Dress Shirt", "category": "top", "color": "White", "description": "Spread collar cotton shirt"},
            {"name": "Pocket Square", "category": "accessories", "color": "Purple", "description": "Silk pocket square with peak fold"},
            {"name": "Derby Shoes", "category": "shoes", "color": "Black", "description": "High-shine leather derbys"}
        ],
        "tags": ["wedding", "guest", "three-piece", "festive"]
    },
    # MEN - PARTY
    {
        "title": "Night Out King",
        "description": "Turn heads at any party with this bold, confidence-boosting ensemble. The contrast between the leather jacket and white tee creates drama.",
        "occasion": "party",
        "gender": "men",
        "season": "all",
        "style": "streetwear",
        "image_url": "https://images.unsplash.com/photo-1681993996237-60d6809d1d97?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwzfHxtZW5zJTIwcGFydHklMjBuaWdodCUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Leather Jacket", "category": "top", "color": "Black", "description": "Slim fit biker jacket"},
            {"name": "Fitted Turtleneck", "category": "top", "color": "White", "description": "Stretch cotton turtleneck"},
            {"name": "Slim Fit Jeans", "category": "bottom", "color": "Black", "description": "Skinny stretch black denim"},
            {"name": "Chelsea Boots", "category": "shoes", "color": "Black", "description": "Leather boots with stacked heel"},
            {"name": "Chain Necklace", "category": "accessories", "color": "Silver", "description": "Layered silver chains"}
        ],
        "tags": ["party", "bold", "leather", "nightlife"]
    },
    # WOMEN - COLLEGE
    {
        "title": "Campus Chic",
        "description": "Smart and stylish without trying too hard. This look transitions seamlessly from lecture halls to coffee shops.",
        "occasion": "college",
        "gender": "women",
        "season": "all",
        "style": "casual",
        "image_url": "https://images.unsplash.com/photo-1640276933838-7ff8c06aa629?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NTYxNzV8MHwxfHNlYXJjaHwyfHx3b21lbnMlMjBjb2xsZWdlJTIwc3R1ZGVudCUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Oversized Button-Up", "category": "top", "color": "White", "description": "Relaxed fit cotton shirt"},
            {"name": "Mini Skirt", "category": "bottom", "color": "Black", "description": "A-line pleated mini skirt"},
            {"name": "Platform Sneakers", "category": "shoes", "color": "White", "description": "Chunky sole canvas sneakers"},
            {"name": "Tote Bag", "category": "accessories", "color": "Canvas", "description": "Large structured tote for books"}
        ],
        "tags": ["campus", "chic", "effortless", "minimal"]
    },
    {
        "title": "Autumn Academia",
        "description": "Dark academia meets modern comfort. Layered textures and warm tones create an intellectual yet fashionable statement.",
        "occasion": "college",
        "gender": "women",
        "season": "fall",
        "style": "minimalist",
        "image_url": "https://images.unsplash.com/photo-1644781698530-257e41ea9ade?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NTYxNzV8MHwxfHNlYXJjaHwxfHx3b21lbnMlMjBjb2xsZWdlJTIwc3R1ZGVudCUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Camel Overcoat", "category": "top", "color": "Camel", "description": "Mid-length wool blend coat"},
            {"name": "Turtleneck", "category": "top", "color": "Black", "description": "Slim fit ribbed turtleneck"},
            {"name": "Plaid Mini Skirt", "category": "bottom", "color": "Navy Plaid", "description": "Pleated tartan mini"},
            {"name": "Knee-High Socks", "category": "accessories", "color": "Black", "description": "Ribbed cotton knee-highs"},
            {"name": "Lace-Up Boots", "category": "shoes", "color": "Black", "description": "Chunky platform lace-ups"}
        ],
        "tags": ["academia", "autumn", "layered", "intellectual"]
    },
    # WOMEN - CASUAL
    {
        "title": "Boho Flow",
        "description": "Free-spirited and artistic. This flowing ensemble captures effortless beauty with its relaxed proportions and natural patterns.",
        "occasion": "casual",
        "gender": "women",
        "season": "summer",
        "style": "bohemian",
        "image_url": "https://images.unsplash.com/photo-1768289222319-5291d85fd640?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjA1OTV8MHwxfHNlYXJjaHw0fHx3b21lbnMlMjBjYXN1YWwlMjBvdXRmaXQlMjBmYXNoaW9ufGVufDB8fHx8MTc3NjM0NjgwMXww&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Printed Tunic", "category": "top", "color": "Blue/Cream", "description": "Flowing V-neck tunic with leaf print"},
            {"name": "Wide Leg Pants", "category": "bottom", "color": "Navy", "description": "Flowy palazzo pants"},
            {"name": "Sandals", "category": "shoes", "color": "Tan", "description": "Flat leather sandals"},
            {"name": "Hoop Earrings", "category": "accessories", "color": "Gold", "description": "Medium gold hoops"}
        ],
        "tags": ["boho", "flowy", "printed", "comfortable"]
    },
    {
        "title": "Pattern Play",
        "description": "Make a statement with coordinated prints. This co-ord set eliminates outfit anxiety while looking incredibly put-together.",
        "occasion": "casual",
        "gender": "women",
        "season": "summer",
        "style": "casual",
        "image_url": "https://images.unsplash.com/photo-1766043071333-5d82991da1ea?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjA1OTV8MHwxfHNlYXJjaHwxfHx3b21lbnMlMjBjYXN1YWwlMjBvdXRmaXQlMjBmYXNoaW9ufGVufDB8fHx8MTc3NjM0NjgwMXww&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Printed Crop Top", "category": "top", "color": "Multicolor Floral", "description": "Short sleeve printed crop blouse"},
            {"name": "Matching Culottes", "category": "bottom", "color": "Multicolor Floral", "description": "Wide-leg cropped pants in matching print"},
            {"name": "Block Heels", "category": "shoes", "color": "Nude", "description": "Low block heel strappy sandals"},
            {"name": "Bangle Set", "category": "accessories", "color": "Gold", "description": "Stacked thin gold bangles"}
        ],
        "tags": ["co-ord", "printed", "matching", "summer"]
    },
    # WOMEN - DATE
    {
        "title": "Romantic Evening",
        "description": "Elegant and alluring without overdoing it. This outfit lets your personality shine through with just the right amount of sophistication.",
        "occasion": "date",
        "gender": "women",
        "season": "all",
        "style": "elegant",
        "image_url": "https://images.unsplash.com/photo-1596662678434-186ae19d2879?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NTYxODd8MHwxfHNlYXJjaHwxfHx3b21lbnMlMjBlbGVnYW50JTIwZGF0ZSUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY2OTB8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Midi Dress", "category": "top", "color": "Emerald", "description": "Fitted satin midi with subtle draping"},
            {"name": "Strappy Heels", "category": "shoes", "color": "Gold", "description": "Delicate ankle-strap stilettos"},
            {"name": "Clutch", "category": "accessories", "color": "Black", "description": "Compact leather envelope clutch"},
            {"name": "Drop Earrings", "category": "accessories", "color": "Gold", "description": "Elegant crystal drop earrings"}
        ],
        "tags": ["romantic", "elegant", "evening", "sophisticated"]
    },
    {
        "title": "Chic Minimalist Date",
        "description": "Less is more. This clean, modern silhouette exudes quiet confidence and effortless sophistication for any date setting.",
        "occasion": "date",
        "gender": "women",
        "season": "all",
        "style": "minimalist",
        "image_url": "https://images.unsplash.com/photo-1618333453067-769b06a8a9a9?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NTYxODd8MHwxfHNlYXJjaHwyfHx3b21lbnMlMjBlbGVnYW50JTIwZGF0ZSUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY2OTB8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Slip Dress", "category": "top", "color": "Champagne", "description": "Bias-cut satin slip dress"},
            {"name": "Pointed-Toe Mules", "category": "shoes", "color": "Black", "description": "Low-heel leather mules"},
            {"name": "Delicate Chain Necklace", "category": "accessories", "color": "Gold", "description": "Fine layered gold chains"},
            {"name": "Mini Bag", "category": "accessories", "color": "Black", "description": "Structured micro handbag"}
        ],
        "tags": ["minimalist", "date", "slip-dress", "effortless"]
    },
    # WOMEN - FORMAL
    {
        "title": "Boss Mode",
        "description": "Command respect with this sharp, tailored power suit. Modern cuts and clean lines create an authoritative yet feminine silhouette.",
        "occasion": "formal",
        "gender": "women",
        "season": "all",
        "style": "formal",
        "image_url": "https://images.unsplash.com/photo-1614786269829-d24616faf56d?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjAxODF8MHwxfHNlYXJjaHw0fHx3b21lbnMlMjBmb3JtYWwlMjBidXNpbmVzcyUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Tailored Blazer", "category": "top", "color": "Black", "description": "Structured single-button blazer"},
            {"name": "Turtleneck", "category": "top", "color": "Black", "description": "Slim ribbed turtleneck"},
            {"name": "High-Waisted Trousers", "category": "bottom", "color": "Black", "description": "Tapered ankle-length trousers"},
            {"name": "Pointed-Toe Pumps", "category": "shoes", "color": "Nude", "description": "Classic stiletto pumps"},
            {"name": "Structured Tote", "category": "accessories", "color": "Black", "description": "Leather work tote"}
        ],
        "tags": ["power", "boss", "tailored", "professional"]
    },
    {
        "title": "Sunset Executive",
        "description": "Business elegance that transitions from boardroom to after-work events. The suit drapes beautifully and moves with confidence.",
        "occasion": "formal",
        "gender": "women",
        "season": "spring",
        "style": "formal",
        "image_url": "https://images.unsplash.com/photo-1767362829004-a2d7da9eaabf?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjAxODF8MHwxfHNlYXJjaHwyfHx3b21lbnMlMjBmb3JtYWwlMjBidXNpbmVzcyUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY4MDF8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Relaxed Blazer", "category": "top", "color": "Charcoal", "description": "Oversized single-breasted blazer"},
            {"name": "Silk Camisole", "category": "top", "color": "Ivory", "description": "V-neck silk cami"},
            {"name": "Wide-Leg Trousers", "category": "bottom", "color": "Charcoal", "description": "Matching wide-leg suit trousers"},
            {"name": "Pointed Mules", "category": "shoes", "color": "Black", "description": "Leather pointed-toe mules"},
            {"name": "Pendant Necklace", "category": "accessories", "color": "Gold", "description": "Simple gold pendant"}
        ],
        "tags": ["executive", "elegant", "wide-leg", "spring"]
    },
    # WOMEN - WEDDING
    {
        "title": "Wedding Belle",
        "description": "Steal the spotlight (respectfully) with this stunning traditional ensemble. Rich fabrics and ornate detailing create a regal presence.",
        "occasion": "wedding",
        "gender": "women",
        "season": "all",
        "style": "elegant",
        "image_url": "https://images.unsplash.com/photo-1756483492084-05cb91948081?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDJ8MHwxfHNlYXJjaHwxfHx3ZWRkaW5nJTIwZ3Vlc3QlMjBvdXRmaXQlMjBmYXNoaW9ufGVufDB8fHx8MTc3NjM0NjgwMXww&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Embroidered Lehenga", "category": "top", "color": "Magenta", "description": "Hand-embroidered silk lehenga choli"},
            {"name": "Dupatta", "category": "accessories", "color": "Magenta/Gold", "description": "Sheer embroidered dupatta"},
            {"name": "Juttis", "category": "shoes", "color": "Gold", "description": "Embellished traditional footwear"},
            {"name": "Statement Jewelry Set", "category": "accessories", "color": "Gold/Kundan", "description": "Necklace and earring set"}
        ],
        "tags": ["wedding", "traditional", "lehenga", "festive"]
    },
    {
        "title": "Enchanted Guest",
        "description": "Graceful and timeless. This flowing silhouette with delicate embellishments is perfect for garden or indoor wedding celebrations.",
        "occasion": "wedding",
        "gender": "women",
        "season": "spring",
        "style": "elegant",
        "image_url": "https://images.unsplash.com/photo-1756483510900-ec43edbafb45?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDJ8MHwxfHNlYXJjaHwyfHx3ZWRkaW5nJTIwZ3Vlc3QlMjBvdXRmaXQlMjBmYXNoaW9ufGVufDB8fHx8MTc3NjM0NjgwMXww&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Anarkali Gown", "category": "top", "color": "Ivory/Blush", "description": "Floor-length embellished anarkali"},
            {"name": "Statement Earrings", "category": "accessories", "color": "Pearl/Gold", "description": "Chandelier pearl earrings"},
            {"name": "Embellished Heels", "category": "shoes", "color": "Rose Gold", "description": "Crystal-studded block heels"},
            {"name": "Clutch", "category": "accessories", "color": "Gold", "description": "Metal box clutch with pearl detail"}
        ],
        "tags": ["wedding", "gown", "graceful", "garden"]
    },
    # WOMEN - PARTY
    {
        "title": "After Dark Glam",
        "description": "Turn every entrance into a moment. Bold, confident, and unapologetically glamorous for a night that demands attention.",
        "occasion": "party",
        "gender": "women",
        "season": "all",
        "style": "elegant",
        "image_url": "https://images.unsplash.com/photo-1673182122218-c63ff9007fc8?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NTYxODd8MHwxfHNlYXJjaHwzfHx3b21lbnMlMjBlbGVnYW50JTIwZGF0ZSUyMG91dGZpdHxlbnwwfHx8fDE3NzYzNDY2OTB8MA&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Bodycon Dress", "category": "top", "color": "Black", "description": "Figure-hugging midi with cutout details"},
            {"name": "Statement Heels", "category": "shoes", "color": "Red", "description": "Strappy platform stilettos"},
            {"name": "Crystal Clutch", "category": "accessories", "color": "Silver", "description": "Crystal-encrusted evening clutch"},
            {"name": "Layered Bracelets", "category": "accessories", "color": "Silver", "description": "Stacked rhinestone bangles"}
        ],
        "tags": ["party", "glam", "bodycon", "nightlife"]
    },
    {
        "title": "Blue Elegance",
        "description": "Sophisticated with a touch of drama. The rich blue fabric and ornate details create an unforgettable silhouette for special occasions.",
        "occasion": "party",
        "gender": "women",
        "season": "winter",
        "style": "elegant",
        "image_url": "https://images.unsplash.com/photo-1756483492038-974f2a2ff341?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDJ8MHwxfHNlYXJjaHwzfHx3ZWRkaW5nJTIwZ3Vlc3QlMjBvdXRmaXQlMjBmYXNoaW9ufGVufDB8fHx8MTc3NjM0NjgwMXww&ixlib=rb-4.1.0&q=85",
        "items": [
            {"name": "Embroidered Jacket", "category": "top", "color": "Navy/Gold", "description": "Ornate cropped jacket with gold work"},
            {"name": "Flowing Skirt", "category": "bottom", "color": "Navy Blue", "description": "Full-length pleated silk skirt"},
            {"name": "Embellished Sandals", "category": "shoes", "color": "Gold", "description": "Jeweled flat sandals"},
            {"name": "Maang Tikka", "category": "accessories", "color": "Gold", "description": "Traditional forehead jewelry"}
        ],
        "tags": ["elegant", "blue", "ornate", "occasion"]
    },
]


@api_router.get("/")
async def root():
    return {"message": "AuraFit API is running"}

@api_router.post("/seed")
async def seed_database():
    return {
        "message": "Using in-memory data. No database needed.",
        "count": len(SEED_OUTFITS)
    }
@api_router.get("/stats")
async def get_stats():
    return {
        "total_outfits": len(SEED_OUTFITS),
        "message": "Static data mode"
    }
# @api_router.post("/seed")
# async def seed_database():
#     # existing = await db.outfits.count_documents({})
#     if existing > 0:
#         return {"message": f"Database already seeded with {existing} outfits", "count": existing}

#     outfits = []
#     for data in SEED_OUTFITS:
#         outfit = Outfit(
#             title=data["title"],
#             description=data["description"],
#             occasion=data["occasion"],
#             gender=data["gender"],
#             season=data["season"],
#             style=data["style"],
#             image_url=data["image_url"],
#             items=[ClothingItem(**item) for item in data["items"]],
#             tags=data["tags"],
#         )
#         outfits.append(outfit.model_dump())

#     # await db.outfits.insert_many(outfits)
#     return {"message": f"Seeded {len(outfits)} outfits", "count": len(outfits)}


# @api_router.get("/outfits")
# async def get_outfits(
#     occasion: Optional[str] = Query(None),
#     gender: Optional[str] = Query(None),
#     season: Optional[str] = Query(None),
#     style: Optional[str] = Query(None),
#     limit: int = Query(3, ge=1, le=10),
# ):
#     query = {}
#     if occasion:
#         query["occasion"] = occasion
#     if gender:
#         query["gender"] = gender
#     if season and season != "all":
#         query["season"] = {"$in": [season, "all"]}
#     if style:
#         query["style"] = style

#     outfits = await db.outfits.find(query, {"_id": 0}).to_list(limit)
#     return {"outfits": outfits, "count": len(outfits)}
@api_router.get("/outfits")
async def get_outfits(
    occasion: Optional[str] = None,
    gender: Optional[str] = None,
    season: Optional[str] = None,
    style: Optional[str] = None,
    limit: int = 3,
):
    filtered = []

    for o in SEED_OUTFITS:
        if occasion and o["occasion"] != occasion:
            continue
        if gender and o["gender"] != gender:
            continue
        if style and o["style"] != style:
            continue
        if season and season != "all" and o["season"] not in [season, "all"]:
            continue

        filtered.append(o)

    return {
        "outfits": filtered[:limit],
        "count": len(filtered[:limit])
    }

# @api_router.get("/outfits/{outfit_id}")
# async def get_outfit(outfit_id: str):
#     outfit = await db.outfits.find_one({"id": outfit_id}, {"_id": 0})
#     if not outfit:
#         return {"error": "Outfit not found"}
#     return outfit

@api_router.get("/filters")
async def get_filters():
    occasions = list(set(o["occasion"] for o in SEED_OUTFITS))
    genders = list(set(o["gender"] for o in SEED_OUTFITS))
    seasons = list(set(o["season"] for o in SEED_OUTFITS))
    styles = list(set(o["style"] for o in SEED_OUTFITS))

    return {
        "occasions": sorted(occasions),
        "genders": sorted(genders),
        "seasons": sorted(seasons),
        "styles": sorted(styles),
    }

# @api_router.get("/stats")
# async def get_stats():
#     total = await db.outfits.count_documents({})
#     pipeline = [{"$group": {"_id": "$occasion", "count": {"$sum": 1}}}]
#     occasion_counts = await db.outfits.aggregate(pipeline).to_list(100)
#     return {
#         "total_outfits": total,
#         "by_occasion": {item["_id"]: item["count"] for item in occasion_counts},
#     }


app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# @app.on_event("startup")
# async def startup_event():
#     existing = await db.outfits.count_documents({})
#     if existing == 0:
#         logger.info("No outfits found. Auto-seeding database...")
#         outfits = []
#         for data in SEED_OUTFITS:
#             outfit = Outfit(
#                 title=data["title"],
#                 description=data["description"],
#                 occasion=data["occasion"],
#                 gender=data["gender"],
#                 season=data["season"],
#                 style=data["style"],
#                 image_url=data["image_url"],
#                 items=[ClothingItem(**item) for item in data["items"]],
#                 tags=data["tags"],
#             )
#             outfits.append(outfit.model_dump())
#         await db.outfits.insert_many(outfits)
#         logger.info(f"Seeded {len(outfits)} outfits")
#     else:
#         logger.info(f"Database has {existing} outfits")


# @app.on_event("shutdown")
# async def shutdown_db_client():
#     client.close()
