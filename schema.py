from pydantic import BaseModel, Field


class Location(BaseModel):
    latitude: float = Field(..., description="Latitude of the location")
    longitude: float = Field(..., description="Longitude of the location")
    address: str = Field(..., description="Address of the location")
    postal_code: str = Field(..., description="Postal code of the location")
    city: str = Field(..., description="City of the location")

class Store(BaseModel):
    name: str = Field(..., description="Name of the store")
    chain: str = Field(..., description="Name of the chain the store belongs to")
    number_of_visits: int = Field(..., description="Number of visits to the store")
    location: Location = Field(..., description="Location details of the store")
    
