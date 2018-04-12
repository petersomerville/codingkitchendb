from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func

from base import Base, inverse_relationship, create_tables


class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)

    api = Column(String, unique=True)
    first = Column(String)
    last = Column(String)
    gender = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_person(self, json_data):
        self.api = json_data['api']
        self.first = json_data['first']
        self.last = json_data['last']
        self.gender = json_data['gender']


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)

    api = Column(String, unique=True)
    name = Column(String)
    founded_on = Column(String)
    total_assets = Column(Integer)
    revenue = Column(Integer)
    operating_income = Column(Integer)
    net_income = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_company(self, json_data):
        self.api = json_data['api']
        self.name = json_data['name']
        self.founded_on = json_data['founded_on']
        self.total_assets = json_data['total_assets']  
        self.revenue = json_data['revenue']  
        self.operating_income = json_data['operating_income']  
        self.net_income = json_data['net_income']  


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)

    api = Column(String, unique=True)
    name = Column(String)
    company = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_department(self, json_data):
        self.api = json_data['api']
        self.name = json_data['name']
        self.company = json_data['company']


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)

    api = Column(String, unique=True)
    name = Column(String)
    abbreviation = Column(String)
    gdp = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_state(self, json_data):
        self.api = json_data['api']
        self.name = json_data['name']
        self.abbreviation = json_data['abbreviation']
        self.gdp = json_data['gdp']  
 

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)

    api = Column(String, unique=True)
    name = Column(String)
    zipcode = Column(String)
    population = Column(Integer)
    is_capital = Column(Integer)
    state = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_city(self, json_data):
        self.api = json_data['api']
        self.name = json_data['name']
        self.zipcode = json_data['zipcode']
        self.population = json_data['population']
        self.is_capital = json_data['is_capital']
        self.state = json_data['state']  


class League(Base):
    __tablename__ = 'leagues'
    id = Column(Integer, primary_key=True)

    api = Column(String, unique=True)
    name = Column(String)
    sport = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_league(self, json_data):
        self.api = json_data['api']
        self.name = json_data['name']
        self.sport = json_data['sport']  


class Club(Base):
    __tablename__ = 'clubs'
    id = Column(Integer, primary_key=True)

    api = Column(String, unique=True)
    name = Column(String)
    league = Column(String)
    city = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_club(self, json_data):
        self.api = json_data['api']
        self.name = json_data['name']
        self.league = json_data['league']
        self.city = json_data['city'] 

class Exchange(Base):
    __tablename__ = 'exchanges'
    id = Column(Integer, primary_key=True)

    api = Column(String, unique=True)
    name = Column(String)
    city = Column(String)
    address = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_exchange(self, json_data):
        self.api = json_data['api']
        self.name = json_data['name']
        self.city = json_data['city']
        self.address = json_data['address'] 

if __name__ != '__main__':
    create_tables()

