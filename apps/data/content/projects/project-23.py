"""
Project #23: Pemilu 2021 Data Hub
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Pemilu 2021 Data Hub
project_data = {
    "id": 23,
    "title": """Pemilu 2021 Data Hub""",
    "headline": """Live 2021 Indonesia Election data at your fingertips with Django REST APIs.""",
    "description": ['This API collection is your VIP pass to Indonesia’s 2021 Election data—candidate names, voting stats, all in real-time glory.', 'Powered by Django REST Framework, it’s built tough with clean endpoints and pro-level error handling.', 'Perfect for devs cooking up election trackers or diving deep into vote analysis with flexible, detailed data.'],
    "images": {
        "pemilu_2021_api.webp": f"{settings.PROJECT_BASE_IMG_URL}/pemilu_2021_api.webp"
    },
    "is_featured": False,
    "features": [{'title': 'Versatile Endpoints', 'description': 'Scoop up candidate names, dispute stats, or voting details effortlessly.'}, {'title': 'Bulletproof Handling', 'description': 'Error-proof design keeps your app running like a dream.'}, {'title': 'Deep Data Dives', 'description': 'Grab election insights at any level for epic analysis.'}],
    "tech_stack": [
        SkillsData.tech_stack["python"],
        SkillsData.tech_stack["django_rest_framework"]
    ],
    "github_url": "https://github.com/PeakPy/realcount-pemilu-2021",
    "demo_url": "",
    "status": "completed",
    "created_at": None,
    "updated_at": datetime.strptime("2021-03-01T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "API, Election, Data, Indonesia",
    "tags": [
        "API",
        "Pemilu 2021",
        "Election Data",
        "Django REST Framework",
        "Python",
        "Indonesia",
        "Voting Stats",
        "Candidate Data",
        "Real-time Data"
    ],
    "priority": 1,
    "slug": ""
}
