To generalize the DFS solution by given a DFS problem, simply define the following conditions:
1. SolutionRequirementCondition
2. NextElementAvailableCondition
3. NextElementRollbackCondition

```
//following is the generalized DFS approach
define NextElement
define Result
define Stack
define ProblemDependentStateInfo

while (NextElementAvailableCondition is true):

    push NextElement on stack           //forward operations
    update ProblemDependentStateInfo    //forward operations

    update NextElement to next possible value
    if SolutionRequirementCondition is True:
        add Stack/ProblemDependentStateInfo snapshot to Result
        pop/update Stack/ProblemDependentStateInfo                  //rollback operations
        (different strategy to update NextElement, or may not necessary, to diff the value from "forward operation")

    while (NextElementRollbackCondition is true and Stack is not empty):
        pop/update Stack/ProblemDependentStateInfo                  //rollback operations
        update NextElement to next possible value

return Result
```