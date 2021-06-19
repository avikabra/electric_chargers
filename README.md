# electric_chargers
Optimisation Research Problem led by IIT Chandigarh on how to ideally place electric chargers around Chandigarh </br>

### Initial brainstorming - 14 Jun 2021 ### </br>
Tentative model: linear programming, traditional constraint satisfaction problem </br>
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
