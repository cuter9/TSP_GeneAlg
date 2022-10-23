from geneal.applications.tsp.travelling_salesman_problem import TravellingSalesmanProblemSolver
# from geneal.applications.tsp.examples.world_capitals.graph import G
from geneal.applications.tsp.helpers import plot_cities
# from geneal.applications.tsp.examples.world_capitals import world_capitals_dict
from examples.world_cities import cities_of, create_graph_of
# from examples.world_cities.graph import create_graph_of

city_id = 2         # select the cities for tour search
state = ''
match city_id:
    case 1:
        country_name = 'WorldCapitals'
    case 2:
        country_name = 'Taiwan'
    case 3:
        country_name = 'Germany'
    case 4:
        country_name = 'Japan'
    case 5:
        country_name = 'China'
        state = 'Jiangsu'
    case 6:
        country_name = 'United States'
        state = 'New York'
world_cities_dict = cities_of(country_name, state)
G = create_graph_of(world_cities_dict)

# selection_strategy : 'roulette_wheel', 'random', 'two_by_two', 'tournament'
# mutation_strategy :   '2-opt', 'random_swap', 'random_inversion', 'random_gene_nearest_neighbour',
#                       'worst_gene_random', 'worst_gene_nearest_neighbour', 'select_any_mutation'
tsp_solver = TravellingSalesmanProblemSolver(
    graph=G,
    pop_size=100,  # population size (number of individuals)
    max_gen=2000,  # maximum number of generations
    mutation_rate=0.01,  # mutation rate to apply to the population
    selection_rate=0.7,  # percentage of the population to select for mating
    selection_strategy='tournament',  # strategy to use for selection.
    mutation_strategy='2-opt'  # strategy to use for mutation. see below for more details.
)

tsp_solver.solve()

# plot_cities(us_cities_dict, tsp_solver,
#             lon=lambda x: x["CapitalLongitude"], lat=lambda x: x["CapitalLatitude"],
#             name=lambda x: x["ContinentName"] + ", " + x["CountryName"])

plot_cities(world_cities_dict, tsp_solver,
            lon=lambda x: x['lng'], lat=lambda x: x['lat'],
            name=lambda x: x['country'] + ", " + x['city'])
