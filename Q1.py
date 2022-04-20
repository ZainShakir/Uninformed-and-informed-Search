import networkx as nx
import queue


class searching_algos:
    
    heuristics= {"Arad" : 366 ,"Bucharest" : 0,"Craiova" : 160,"Drobeta" : 242,"Eforie" : 161,"Fagaras" : 176,"Giurgiu" : 77,"Hirsova" : 151,
    "Iasi" : 226,"Lugoj" : 244,"Mehadia" : 241,"Neamt" : 234,"Oradea" : 380,"Pitesti" : 100,"Rimnicu Vilcea" : 193,"Sibiu" : 253,
    "Timisoara" : 329,"Urziceni" : 80,"Vaslui" : 199,"Zerind" : 374}
    result={}
    

    
    def __init__(self):
        self.graph=nx.Graph()
        self.graph.add_edge('Arad', 'Timisoara', weight=118)
        self.graph.add_edge('Arad', 'Sibiu', weight=140) 
        self.graph.add_edge('Arad', 'Zerind', weight=75)
        self.graph.add_edge('Zerind', 'Oradea', weight=71)
        self.graph.add_edge('Oradea', 'Sibiu', weight=151)
        self.graph.add_edge('Timisoara', 'Lugoj', weight=111)
        self.graph.add_edge('Sibiu', 'Fagaras', weight=99)
        self.graph.add_edge('Sibiu', 'Rimnicu Vilcea', weight=80)
        self.graph.add_edge('Rimnicu Vilcea', 'Craiova', weight=146)
        self.graph.add_edge('Rimnicu Vilcea', 'Pitesti', weight=97)
        self.graph.add_edge('Lugoj', 'Mehadia', weight=70)
        self.graph.add_edge('Mehadia', 'Drobeta', weight=75)
        self.graph.add_edge('Drobeta', 'Craiova', weight=120)
        self.graph.add_edge('Craiova', 'Pitesti', weight=138)
        self.graph.add_edge('Pitesti', 'Bucharest', weight=101)
        self.graph.add_edge('Fagaras', 'Bucharest', weight=211)
        self.graph.add_edge('Bucharest', 'Giurgiu', weight=90)
        self.graph.add_edge('Bucharest', 'Urziceni', weight=85)
        self.graph.add_edge('Urziceni', 'Hirsova', weight=98)
        self.graph.add_edge('Urziceni', 'Vaslui', weight=142)
        self.graph.add_edge('Hirsova', 'Eforie', weight=86)
        self.graph.add_edge('Vaslui', 'Iasi', weight=92)
        self.graph.add_edge('Iasi', 'Neamt', weight=87)
        self.Map=nx.to_dict_of_dicts(self.graph)

        

        
    def Breadth_first_Search(self,start,goal):
        visited=[]
        path=[]
        path_cost=0
        output = {}
        que=queue.Queue()
        if(start==goal):
            print("Starting city and destination city are same")
            print(f"Path Cost={path_cost}")
        else:
            que.put([0,start])
            visited.append(start)
            while not que.empty():
                temp=que.get()
                cost=temp[0]
                cur_city=temp[1]
                path.append(cur_city)
                for cities in self.Map[cur_city]:
                    if(cities not in visited):
                        visited.append(cities)
                        que.put([self.Map[cur_city][cities]['weight'],cities])
                if(cur_city==goal):
                    path_cost+=cost
                    output['cost']=path_cost
                    output['path']=path
                    self.result['breadth_first'] = output
                    break;
                else:
                    path_cost+=cost
                    
                    
    def Greedy_Best_first_Search(self,start,goal):
        visited=[]
        path=[]
        path_cost=0
        output={}

        que=queue.PriorityQueue()
        que.put([0,start])
        visited.append(start)
        if(start==goal):
            print("Starting city and destination city are same")
            print(f"Path Cost={path_cost}")
        else:     
            while not que.empty():
                temp=que.get()        
                cur_city=temp[1]
                path.append(cur_city)
                if(cur_city==goal):
                    for i in range (0,len(path)-1):
                        if(self.graph.has_edge(path[i], path[i+1])==False):
                            path_cost=-1
                            break
                        else:
                            path_cost+=self.Map[path[i]][path[i+1]]['weight']
                    if(path_cost != -1):
                        output['cost']=path_cost
                        output['path']=path
                        self.result['best_first'] = output
                    else:
                        print("Path unreachable")
                    break;
                else:
                    for cities in self.Map[cur_city]:
                        if(cities not in visited):
                            visited.append(cities)
                            que.put([self.heuristics[cities],cities])
                            
    def Uniform_cost_search(self,start,goal):
        visited=[]
        path=[]
        output={}
        que=queue.PriorityQueue()
        que.put([0,start,[start]])
        visited.append(start)
        while not que.empty():
            temp=que.get()
            cost=temp[0]
            cur_city=temp[1]
            path=temp[2]
            if(cur_city==goal):
                output['cost']=cost
                output['path']=path
                self.result['uniform_cost'] = output
                break;
            else:
                for cities in self.Map[cur_city]:
                        que.put([cost+self.Map[cur_city][cities]['weight'],cities,path+[cities]])
                        
                        

    path = []  
    def Depth_limited_search(self,start,goal,depth):
        if(start==goal):
            return True
        if(depth<0):
            return False
        
        for cities in self.Map[start]:
            if self.Depth_limited_search(cities,goal,depth-1):
                self.path.append(cities)
                return True
        return False
    
    def iterative_DDFS(self,start,goal,depth):
        for x in range(depth):
            if self.Depth_limited_search(start, goal, x):
                self.path.append(start)
                self.path.reverse()
                return self.path
        return ("Path no found")
                
    def IDDFS_COST(self,start,goal):
        output={}
        cost=0
        path1=self.iterative_DDFS(start, goal, 7) 
        for i in range (0,len(path1)-1):
            cost+=self.Map[path1[i]][path1[i+1]]['weight']
        output['cost']=cost
        output['path']=path1
        self.result['iterative_deepening']=output
        
        
    def display(self):
        res = sorted(self.result.items(), key=lambda x: x[1]['cost'])
        for search in res:
            print("\nResult Of "+search[0] + " Search \n")
            print("path==> ", search[1]['path'])
            print("cost==> ", search[1]['cost'])    
            
     
romania=searching_algos()
start=input("Enter Start Node:")
goal=input("Enter Goal Node:")

if(romania.graph.has_node(start)==True and romania.graph.has_node(goal)==True):
    romania.Breadth_first_Search(start, goal)           
    romania.Greedy_Best_first_Search(start, goal)   
    romania.Uniform_cost_search(start, goal)
    romania.IDDFS_COST(start, goal)
    romania.display()
else:
    print("Graph doesn't have any one of the above nodes")

        



         


        
    
    
