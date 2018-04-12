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
            if 'detail' not in json_data:
                person.parse_person(json_data)
                return self.db.save(person)
            else:
                return results[0]

    def get_company(self, i):
        company_url = 'http://data.coding.kitchen/api/company/{}'.format(i) 
        results = self.db.open().query(Company).filter(Company.url == company_url).all()
        if len(results) == 0:
            json_data = self.get_json(company_url)
            company = Company()
            if 'detail' not in json_data:
                company.parse_company(json_data)
                return self.db.save(company)
            else:
                return results[0]

    def get_department(self, i):
        department_url = 'http://data.coding.kitchen/api/department/{}'.format(i) 
        results = self.db.open().query(Department).filter(Department.url == department_url).all()
        if len(results) == 0:
            json_data = self.get_json(department_url)
            department = Department()
            if 'detail' not in json_data:
                department.parse_department(json_data)
                return self.db.save(department)
            else:
                return results[0]

    def get_state(self, i):
        state_url = 'http://data.coding.kitchen/api/state/{}'.format(i) 
        results = self.db.open().query(State).filter(State.url == state_url).all()
        if len(results) == 0:
            json_data = self.get_json(state_url)
            state = State()
            if 'detail' not in json_data:
                state.parse_state(json_data)
                return self.db.save(state)
            else:
                return results[0]

    def get_city(self, i):
        city_url = 'http://data.coding.kitchen/api/city/{}'.format(i) 
        results = self.db.open().query(City).filter(City.url == city_url).all()
        if len(results) == 0:
            json_data = self.get_json(city_url)
            city = City()
            if 'detail' not in json_data:
                city.parse_city(json_data)
                return self.db.save(city)
            else:
                return results[0]

    def get_league(self, i):
        league_url = 'http://data.coding.kitchen/api/league/{}'.format(i) 
        results = self.db.open().query(League).filter(League.url == league_url).all()
        if len(results) == 0:
            json_data = self.get_json(league_url)
            league = League()
            if 'detail' not in json_data:
                league.parse_league(json_data)
                return self.db.save(league)
            else:
                return results[0]

    def get_club(self, i):
        club_url = 'http://data.coding.kitchen/api/club/{}'.format(i) 
        results = self.db.open().query(Club).filter(Club.url == club_url).all()
        if len(results) == 0:
            json_data = self.get_json(club_url)
            club = Club()
            if 'detail' not in json_data:
                club.parse_club(json_data)
                return self.db.save(club)
            else:
                return results[0]    
        
    def get_exchange(self, i):
        exchange_url = 'http://data.coding.kitchen/api/exchange/{}'.format(i) 
        results = self.db.open().query(Exchange).filter(Exchange.url == exchange_url).all()
        if len(results) == 0:
            json_data = self.get_json(exchange_url)
            exchange = Exchange()
            if 'detail' not in json_data:
                exchange.parse_exchange(json_data)
                return self.db.save(exchange)
            else:
                return results[0]   