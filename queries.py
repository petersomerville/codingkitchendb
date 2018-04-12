from ckds import CKDS, Person, Company, Department, State, City, League, Club, Exchange
from pprint import pprint

ckds = CKDS()

# FIND ALL STATES THAT HAVE EXCHANGES

# FIND ALL THE PEOPLE WHO ARE UNEMPLOYED

# FIND ALL THE PEOPLE WHO ARE CURRENTLY PART OF A CLUB

# PRINT OUT ALL THE STATES THAT HAVE RUGBY TEAMS

# CREATE A FUNCTION THAT TAKES IN AN INDUSTRY AND RETURNS THE TOP FIVE COMPANIES BY REVENUE

# PRINT ALL LEAGUES AND THEN INDENTED ALL TEAM NAMES WITH STATES
league_list = ckds.db.open().query(League).filter().all()
for league in league_list:
    pprint(league.name)
    clubs_list = ckds.db.open().query(Club).filter(Club.league == league.id).all()
    for club in clubs_list:
        cities_list = ckds.db.open().query(City).filter(City.id == club.city).all()
        for city in cities_list:
            states_list = ckds.db.open().query(State).filter(State.abbreviation == city.state).all()
            for state in states_list:
                print('\t >{}, {}'.format(club.name, state.name))

# NAME ALL COMPANIES WITH AN HR DEPARTMENT
# hr_depts = ckds.db.open().query(Department).filter(Department.name == 'Human Resources').all()
# for hr_dept in hr_depts:
#     comp_ids_list = hr_dept.company 
#     comp_list = ckds.db.open().query(Company).filter(Company.id == comp_ids_list).all()
#     for comp in comp_list:
#         pprint(comp.name)

# NAME EACH CITY WITH AN EXCHANGE
# exchanges_list = ckds.db.open().query(Exchange).filter().all()
# for exchange in exchanges_list:
#     city_ids_list = exchange.city
#     cities_list = ckds.db.open().query(City).filter(City.id == city_ids_list).all()
#     for exchange_city in cities_list:
#         print(exchange_city.name)

# NAME COMPANIES WITH REVENUE > 1000
# high_rev_cos = ckds.db.open().query(Company).filter(Company.revenue > 1000).all()
# for high_rev_co in high_rev_cos:
#     pprint(high_rev_co.name)

# NAME ALL STATE CAPITALS
# state_capitals = ckds.db.open().query(City).filter(City.is_capital == 1).all()
# for state_capital in state_capitals:
#     pprint(state_capital.name)

# STATES WITH GDP > 100,000
# rich_states = ckds.db.open().query(State).filter(State.gdp > 100000).all()
# for rich_state in rich_states:
#     pprint(rich_state.name)

# COMPANIES WITH NEGATIVE NET INCOME
# loser_companies = ckds.db.open().query(Company).filter(Company.net_income < 0).all()
# for loser_company in loser_companies:
#     pprint(loser_company.name)

# FIND THE STATE WITH ABBREVIATION SZ
# states_sz = ckds.db.open().query(State).filter(State.abbreviation == 'SZ').one()
# pprint(states_sz.name)

# NAME ALL FEMALE PEOPLE
# female_people = ckds.db.open().query(Person).filter(Person.gender == 'F').all()
# for female_person in female_people:
#     pprint('{} {}'.format(female_person.first, female_person.last))

# NAME ALL PEOPLE WITH LAST NAME FRANKS
# franks_people = ckds.db.open().query(Person).filter(Person.last == "Franks").all()
# for franks_person in franks_people:
#     pprint('{} {}'.format(franks_person.first, franks_person.last))