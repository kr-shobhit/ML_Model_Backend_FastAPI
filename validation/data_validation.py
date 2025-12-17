from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=100, description= "Enter Age of User", examples=[67, 18, 20])]
    weight: Annotated[float, Field(..., gt=0, description="Enter Weight of User in Kgs", examples=[55.0, 87, 67.9])]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Enter Height of User in Mtr", examples=[1.08, 2.1, 1.09])]
    income_lpa: Annotated[float, Field(..., gt=0, description="Enter Income of User in Lakhs", examples=[2.9, 13.87, 12])]
    smoker: Annotated[bool, Field(..., description="Enter Smoking Habits")]
    city: Annotated[str, Field(..., description="Enter City of User")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], Field(..., description="Enter Occupation of User")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2), 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'high'
        elif self.smoker and self.bmi > 27:
            return 'medium'
        else : return 'low'
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'young'
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return 'middle_aged'
        else : return 'senior'

    @computed_field
    @property
    def city_tier(self) -> int:
        tier_1_cities = ["mumbai", "delhi", "bangalore", "chennai", "kolkata","hyderabad", "pune"]

        tier_2_cities = ["jaipur", "chandigarh", "indore", "lucknow", "patna", "ranchi","visakhapatnam", "coimbatore", "bhopal", "nagpur", "vadodara","surat", "rajkot", "jodhpur", "raipur", "amritsar", "varanasi","agra", "dehradun", "mysore", "jabalpur", "guwahati","thiruvananthapuram", "ludhiana", "nashik", "allahabad","udaipur", "aurangabad", "hubli", "belgaum", "salem","vijayawada", "tiruchirappalli", "bhavnagar", "gwalior","dhanbad", "bareilly", "aligarh", "gaya", "kozhikode","warangal", "kolhapur", "bilaspur", "jalandhar", "noida","guntur", "asansol", "siliguri"]

        if self.city.lower() in tier_1_cities:
            return 1
        elif self.city.lower() in tier_2_cities:
            return 2
        else: return 3