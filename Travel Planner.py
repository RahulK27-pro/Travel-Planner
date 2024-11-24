import heapq

class AttractionNode:
    def __init__(self, name, time_cost, budget_cost, interest_score, mandatory=False):
        self.name = name
        self.time_cost = time_cost  
        self.budget_cost = budget_cost
        self.interest_score = interest_score
        self.mandatory = mandatory
        self.children = []  
        self.description = "" 
        self.location = ""  

    def add_child(self, node, is_and=True):
        """Add child node with AND/OR relationship"""
        self.children.append((node, is_and))

    def __repr__(self):
        return self.name

class AOStarSearch:
    def __init__(self, start_node, num_days, available_budget):
        self.start_node = start_node
        self.available_budget = available_budget
        self.available_time = num_days * 8 

    def heuristic(self, node):
        """Heuristic function to rank nodes by time, budget, and interest score"""
        return node.time_cost + node.budget_cost - node.interest_score

    def ao_star_search(self):
        open_list = [(self.heuristic(self.start_node), 0, 0, self.start_node)]  
        heapq.heapify(open_list)
        visited = set()

        best_plan = []
        best_total_budget = 0

        while open_list:
            heuristic, total_time, total_budget, current = heapq.heappop(open_list)

            if current in visited:
                continue
            visited.add(current)

        
            if total_time <= self.available_time and total_budget <= self.available_budget:
                best_plan.append(current.name)
                best_total_budget = total_budget      

            for child, is_and in current.children:
                new_time = total_time + child.time_cost
                new_budget = total_budget + child.budget_cost
                new_heuristic = heuristic + self.heuristic(child) 

                if new_time <= self.available_time and new_budget <= self.available_budget:
                    heapq.heappush(open_list, (new_heuristic, new_time, new_budget, child))

        return best_plan, best_total_budget


if __name__ == "__main__":
    
    eiffel_tower = AttractionNode("Eiffel Tower", time_cost=2, budget_cost=30, interest_score=10, mandatory=True)
    eiffel_tower.description = "Iconic wrought-iron lattice tower."
    eiffel_tower.location = "Champ de Mars, Paris"

    louvre = AttractionNode("Louvre Museum", time_cost=3, budget_cost=25, interest_score=9)
    louvre.description = "World-famous museum with vast art collections."
    louvre.location = "Rue de Rivoli, Paris"

    boat_ride = AttractionNode("Seine River Boat Ride", time_cost=1, budget_cost=15, interest_score=7)
    boat_ride.description = "Enjoy a scenic boat ride on the Seine River."
    boat_ride.location = "Seine River, Paris"

    notre_dame = AttractionNode("Notre Dame Cathedral", time_cost=2, budget_cost=0, interest_score=8)
    notre_dame.description = "Historic Catholic cathedral with Gothic architecture."
    notre_dame.location = "Île de la Cité, Paris"

    champs_elysees = AttractionNode("Champs-Élysées", time_cost=1, budget_cost=10, interest_score=6)
    champs_elysees.description = "Famous avenue with shops, cafes, and theaters."
    champs_elysees.location = "Champs-Élysées, Paris"

    montmartre = AttractionNode("Montmartre", time_cost=3, budget_cost=20, interest_score=8)
    montmartre.description = "Historic district with Sacré-Cœur Basilica and artistic vibe."
    montmartre.location = "Montmartre, Paris"

    sacre_coeur = AttractionNode("Sacré-Cœur Basilica", time_cost=1.5, budget_cost=5, interest_score=7)
    sacre_coeur.description = "White-domed basilica with panoramic views of the city."
    sacre_coeur.location = "Montmartre, Paris"

    versailles = AttractionNode("Palace of Versailles", time_cost=4, budget_cost=40, interest_score=10)
    versailles.description = "Opulent palace and gardens of the French monarchy."
    versailles.location = "Versailles, France"

    luxembourg_gardens = AttractionNode("Luxembourg Gardens", time_cost=2, budget_cost=5, interest_score=6)
    luxembourg_gardens.description = "Beautiful gardens with fountains, statues, and a palace."
    luxembourg_gardens.location = "Luxembourg Gardens, Paris"

    disneyland = AttractionNode("Disneyland Paris", time_cost=6, budget_cost=60, interest_score=9)
    disneyland.description = "Disney theme park with rides, shows, and characters."
    disneyland.location = "Marne-la-Vallée, France"

    pompidou = AttractionNode("Centre Pompidou", time_cost=2, budget_cost=15, interest_score=6)
    pompidou.description = "Modern art museum with a distinctive industrial design."
    pompidou.location = "Beaubourg, Paris"

    orsay = AttractionNode("Musée d'Orsay", time_cost=3, budget_cost=20, interest_score=9)
    orsay.description = "Museum housing French art from the 19th and early 20th centuries."
    orsay.location = "Rue de la Légion d'Honneur, Paris"


    eiffel_tower.add_child(louvre, is_and=False)
    louvre.add_child(boat_ride, is_and=False)
    louvre.add_child(notre_dame, is_and=False)
    notre_dame.add_child(champs_elysees, is_and=False)
    champs_elysees.add_child(montmartre, is_and=False)
    montmartre.add_child(sacre_coeur, is_and=False)
    sacre_coeur.add_child(versailles, is_and=False)
    versailles.add_child(luxembourg_gardens, is_and=False)
    luxembourg_gardens.add_child(disneyland, is_and=False)
    disneyland.add_child(pompidou, is_and=False)
    pompidou.add_child(orsay, is_and=False)

    
    while True:
        try:
            num_days = int(input("Enter the number of days for your trip: "))
            if num_days > 0:
                break
            else:
                print("Please enter a valid number of days (greater than 0).")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            travel_budget = float(input("Enter your budget for the trip in currency units: "))
            if travel_budget > 0:
                break
            else:
                print("Please enter a valid budget (greater than 0).")
        except ValueError:
            print("Invalid input. Please enter a number.")

    
    planner = AOStarSearch(start_node=eiffel_tower, num_days=num_days, available_budget=travel_budget) 
    best_plan, total_budget = planner.ao_star_search()

    
    print("\nBest Travel Itinerary:")

    
    attraction_map = {
        "Eiffel Tower": eiffel_tower,
        "Louvre Museum": louvre,
        "Seine River Boat Ride": boat_ride,
        "Notre Dame Cathedral": notre_dame,
        "Champs-Élysées": champs_elysees,
        "Montmartre": montmartre,
        "Sacré-Cœur Basilica": sacre_coeur,
        "Palace of Versailles": versailles,
        "Luxembourg Gardens": luxembourg_gardens,
        "Disneyland Paris": disneyland,
        "Centre Pompidou": pompidou,
        "Musée d'Orsay": orsay,
    }

    for activity in best_plan:
        attraction = attraction_map[activity]
        print(f"- {activity} ({attraction.location}): {attraction.description}")

    print(f"\nTotal Cost: {total_budget} currency units")


