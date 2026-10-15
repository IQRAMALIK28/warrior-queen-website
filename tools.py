from typing import TypedDict, List, Dict


# ========== Type Definition - Professional Structure ==========


class ContactInfo(TypedDict):
    """Contact info ka professional structure"""
    whatsapp_number: str
    email: str
    location_short: str
    google_maps_link: str


class SocialInfo(TypedDict):
    instagram_name: str
    instagram_link: str
    facebook_name: str
    facebook_link: str


class PricingInfo(TypedDict):
     free_trial: str
     paid_trial: str
     group_classes: List[str]
     one_on_one: str


# ========== All Data - Sirf Yahan Change Krna Hai ==========

COMPANY_INFO: Dict[str, str] ={
    "brand_name": "Warrior Queen",
    "tagline": "Empowering Women Through Strength & Self-Defence",
    "location":  "Inam Martial Art Academy, Gizri Ave, Lower Gizri, Karachi"
}


CONTACT_INFO: ContactInfo = {
    "whatsapp_number": "+923335029001",
    "email": "zainabkhan.warrior28@gmail.com",
    "location": "Inam Martial Art Academy, online and offline ",
    "google_maps_link": "https://www.google.com/maps/place/Inam+Martial+Art+Academy+Gym+%26+Fitness+Centre/@24.8225054,67.0470527,17z"
}

SOCIAL_INFO: SocialInfo = {
    "instagram_name": "ZK_Warrior_28",
    "instagram_link": "https://www.instagram.com/zk_warrior_28/",
    "facebook_name": "Zainab Khan",
    "facebook_link": "https://www.facebook.com/zainab.khan.829028"
}


TRAINER_INFO: Dict[str, object] = {
    "title": "Head Female Coach - Inam Martial Art Academy",
    "credentials": [
        "Pakistan National Team Representative"
    ],
    "bio": "Empowering females from young girls to senior women"
}



PRICING_INFO: PricingInfo = {
    "free_trial": "Group Free Trial Class - FREE",
    "paid_trial": "Exclusive One_on_One Trial Class - Rs. 3000(Paid)",
    "group_classes": [
        "Private Female Strength Training Group - RS. 15,000 / month",
        "Girls Karate Group - RS. 10,000 per head"
    ],
    "one_on_one": "Exclusive One_on-One (1 Hour,Thrice a Week) - RS. 35,000 / month"
}


SERVICES_LIST: List[str] = [
    "Self Defence Training",
    "Strength Training",
    "Fitness Training",
    "Martial Arts Training",
    "Women Empowerment Workshop"
]    



TRAINING_PROGRAMS: Dict[str, str] = {
  "kids_teens": "KidS & Teens Karate - Strength & Coordination",
  "adult_women": "Adult Women - Strength, Fitness, Self-Defence",
  "women_50_plus": "Women 50+ - Joint Mobility & Functinal Movement",
  "schedule_note": "Har bath ki timing alag hy. Whatsapp par contact karkr confirm kar sakte hain"
}

ACHIEVEMENTS_INFO: Dict[str, object] = {
    "title": "Awards & Certifications",
    "list":[
        "Black Belt 1 Dan in Kyokushin Karate",
        "3rd Bahrain Championship 2023 - 1st place Gold Medal",
        "5th KFW World Championship Riyadah - 1st place Gold Medal",
        "Become First PAKISTANI in Kyokushin Karate History",
        "Kyokushin Karate Championship Spain - Represented Pakistan",
        "GFT - Global Fitness Trainer Certified",
        "Certified Martial Arts Coach",
        "14 Years Experience in Female Fitness Training"
    ],
    "note": "First Female-led Self Defence Academy in Karachi"
}

TRAINER_IMAGES: Dict = [
    "zainab_khan_1.jpg", 
    "zainab_khan_1.jpg", 
    "zainab_khan_3.jpg", 
    "zainab_khan_4.jpg"
]


CORE_TRAINING_AREAS = SERVICES_LIST
TRAINING_AREAS = SERVICES_LIST


# ========== Tool Functions - inko hath na lagayen ==========

def get_company_info() -> Dict[str, str]:
    """Warrior Queen Company info return karta hai"""
    return COMPANY_INFO

def get_contact_info() -> ContactInfo:
    """Contact details return karta hai"""
    return CONTACT_INFO

def get_social_links() -> SocialInfo:
    """Social media links return karta hai"""
    return SOCIAL_INFO

def get_pricing() -> PricingInfo:
    """Sari pricing details return karta hai - 10000, 15000, 35000, 3000"""
    return PRICING_INFO

def get_trainer_info() -> Dict[str, object]:
    """Trainer credentials return karta hai"""
    return TRAINER_INFO

def get_achievements_info() -> Dict[str, object]:
    """Achievement return karta hai"""
    return ACHIEVEMENTS_INFO

def get_training_programs() ->Dict[str,str]:
    """Sare programs return karta hy bina fixeddays ke"""
    return TRAINING_PROGRAMS


def get_services() ->List[str]:
    """Sevices list return kata hai"""
    return SERVICES_LIST

def get_trainer_images():
    return TRAINER_IMAGES


    


