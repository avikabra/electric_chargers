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

LATER
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
