import json, requests
from pprint import pprint
from ck_entities import Person, Company, Department, State, City, League, Club, Exchange
from base import DbManager

class CKDS:
    def __init__(self):
        self.db = DbManager()

    def get_json(self, url):
        print('GET\t<{}>'.format(url))
        response = requests.get(url)
        return json.loads(response.text)

    def get_person(self, i):
        person_url = 'http://data.coding.kitchen/api/person/{}'.format(i) 
        results = self.db.open().query(Person).filter(Person.url == person_url).all()
        if len(results) == 0:
            json_data = self.get_json(person_url)
            person = Person()
            return results[0]

    def get_company(self, i):
        company_url = 'http://data.coding.kitchen/api/company/{}'.format(i) 
        results = self.db.open().query(Company).filter(Company.url == company_url).all()
        if len(results) == 0:
            json_data = self.get_json(company_url)
            company = Company()
            return results[0]

    def get_department(self, i):
        department_url = 'http://data.coding.kitchen/api/department/{}'.format(i) 
        results = self.db.open().query(Department).filter(Department.url == department_url).all()
        if len(results) == 0:
            json_data = self.get_json(department_url)
            department = Department()
            return results[0]

    def get_state(self, i):
        state_url = 'http://data.coding.kitchen/api/state/{}'.format(i) 
        results = self.db.open().query(State).filter(State.url == state_url).all()
        if len(results) == 0:
            json_data = self.get_json(state_url)
            state = State()
            return results[0]

    def get_city(self, i):
        city_url = 'http://data.coding.kitchen/api/city/{}'.format(i) 
        results = self.db.open().query(City).filter(City.url == city_url).all()
        if len(results) == 0:
            json_data = self.get_json(city_url)
            city = City()
            return results[0]

    def get_league(self, i):
        league_url = 'http://data.coding.kitchen/api/league/{}'.format(i) 
        results = self.db.open().query(League).filter(League.url == league_url).all()
        if len(results) == 0:
            json_data = self.get_json(league_url)
            league = League()
            return results[0]

    def get_club(self, i):
        club_url = 'http://data.coding.kitchen/api/club/{}'.format(i) 
        results = self.db.open().query(Club).filter(Club.url == club_url).all()
        if len(results) == 0:
            json_data = self.get_json(club_url)
            club = Club()
            return results[0]    
        
    def get_exchange(self, i):
        exchange_url = 'http://data.coding.kitchen/api/exchange/{}'.format(i) 
        results = self.db.open().query(Exchange).filter(Exchange.url == exchange_url).all()
        if len(results) == 0:
            json_data = self.get_json(exchange_url)
            exchange = Exchange()
            return results[0]   