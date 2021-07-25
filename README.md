# electric_chargers
Optimisation Research Problem led by IIT Chandigarh on how to ideally place electric chargers around Chandigarh </br>

### Initial brainstorming - 14 Jun 2021 ###
Tentative model: linear programming, traditional constraint problem </br>
</br>
Similar papers: </br>
https://www.atlantis-press.com/article/25849537.pdf </br>
</br>
Tentative constraints: </br>
* cost to build charging stations
    * implementation as a constraint: 
    * notes: electric and monetary cost, would need to be predefined. Electric cost would also be variable depending on how busy a certain region is. Ideally though, I would expect each charging station to have an equal cost to build and similar ongoing cost. 
* capacity (how many cars can be charged at once)
    * implementation as a constraint:
    * notes: we could also treat charging stations as individual nodes and allow for them to be placed close together. Problem is that would have a greater cost as opposed to setting multiple stations up in one location. Also needs to be dependent on population density, as well as electric car density
* charging duration
    * implementation as a constraint:
    * notes: could be tough since we introduce time as a variable, then one other constraint would have to be on the car itself
* electric car range
    * implementation as a constraint:
    * note: would have to incorporate multiple electric car models / other charging ports would have to be well within maximum range

### Undergraduate initial presentation notes - 19 Jun 2021 ###
* Important to consider Indian context
    * Ahmdebad as an example 
        * different development levels in one region
        * population resides in the less developed part (sure about this?)
        * river seperates the city, residence on one side of the city and work on the other
    * have to consider the practical as well (mathematical approach considers idealistic first and then the practical)
    * distribution network of power (electrical constraint)
        * two fronts --> reliability and voltage
        * reliability: consumer ease
        * voltage: where can chargers actually be placed

* Divide the problem up
    * contextualize the problem considering Ahmdebad
        * aggregate the CURRENT state of electric charging, power distribution
        * what are deliverables policy makers would like to see?
        * reliance on public charging stations would be high
            * because no point of subsidizing electric cars that you cannot charge
        * ie. CNG-based cars flopped
    * consider the different aspects of the problem
        * socio economic 
        * power distribution
        * network optimization

### Meeting notes - 21 Jun 2021 ###
Yamini Presentation: 
* two different stages 
    * first stage: screening of the candidate locations
    * second stage: optimization through a) cost function, b) accessibility index, c) incorporating the waiting time
</br>

Factors to consider and optimization </br>
ASSUMPTIONS: 
* fast / slow charging stations

NOW:
* electric car range (to address range anxiety)

LATER:
* waiting time for each car at the station (is an optimization problem)
* accessibility index (solves the problem of range anxiety, but doesn't make a large difference because )
</br>

Overview: 
1. Implement stage 1 for a toy model with randomized inputs and constraints
2. Optimize stage 1 in stage 2 for said inputs and constraints
3. Apply to individual cities
</br>

Next Steps:
1. Check document for notes (https://docs.google.com/document/d/1EGx8vX48HEVFUJrC1AG5TfXA7Ka5clb06fd8iwofrC4/edit?ts=60d065a4)
2. Brainstorm individually

### Meeting Notes - 29 Jun 2021 ###
Thoughts on specific implementations of constraints as well as a larger overview on topics was completed. Planning (along with my own comments in red) is highlighted in this document: https://docs.google.com/document/d/1WDhIDYcyqWUILn8Yc8v6_6BNkk9gLeKBngfzhqUvj9s/edit </br>
Next steps going forward are to begin coding; Yamini will share a Github repo and we will begin building the toy model probably with large simplifications. </br>
</br>
Thoughts on papers about optimal EVSE placement: </br>
https://arxiv.org/pdf/1801.02129.pdf
* utilizes a nested logit model (not entirely sure what that is)
    * used to predict charging demand and consumer behavior
* assumptions listed in the introduction, could be worth looking at for the project to see if overlap is evident
* Bayesian model vs Bayesian game?
    * Bayesian game is essentially also governed by a probability distribution since the actions of the consumer are not known
* our approach has us leading into the problem from the perspective of an urban planner
    * what role does the free, competitive market play
* what this work essentially does
    * we can use the nested logit model presented in this paper to evaluate the customer satisfaction of our model
        * considers travel patterns of people to check effectiveness
        * if EVSE placed in high-traffic region, should be more rewarding than if in isolated regions
    * we can look at their placement strategy to see what factors and constraints they considered prior to EVSE placement
* implications for IIT project:
    * provides a method by which effectiveness can be measured
    * introduces relevant constraints and problems in the Western world (may or may not related to India specifically)
    * no toy model is created, so this paper will be increasingly more useful as the toy model is applied to real cities

http://ieeexplore.ieee.org/document/7275344/
* views placing electric chargers as a location optimization problem
* method: mixed integer linear programming
    * hueristic algo as opposed to exact, meaning that the solution might not be optimal, but it is fast and close
    * genetic algorithm is used
        * relates the problem to some type of genetic hueristic
        * it presumably works
* uses MATLAB simulation as a measure of effectivness
* constraints
    * investment cost
    * transportation cost
    * users demand
    * station's capacity
    * coverage of the whole area, convenience
* this solution does not consider roads, but does consider larger sectors
* model is highly generalized, could be a similar approach to the one that we take
* application to a city was also very general, how specific do we want to go?

### Meeting on Jul 5 ###
job - to construct the Bayesian network and probabilities with given data about VSF, transportation network
Bayesian network can be constructed using the Bayesian package from Intro to AI package </br>
Code can be found largely in the `Final1.py` Python file. `bayesian_network.py` contains the Intro to AI template used. </br>
</br>

### Work from Jul 5 - Jul 25 ###
1. Determine candidate locations for the toy model
   * using randomly generated data, use a Bayesian network to probabilistically determine whether different distribution network busses are suitable for electric charger construction consider voltage stability, distance from distribution network, and transportation network congestion.
2. Optimize number of fast charging stations per candidate location
   * done with the scipy optimize package using equations listed in the final report documnet
3. Apply above steps to a real city
   * first find the candidate locations based on same factors, then optimize the number of fast charging stations to cater to waiting time objective function
   * city data along with modified programs can be found in the `real_city` directory

