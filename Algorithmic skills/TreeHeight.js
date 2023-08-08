// https://app.codility.com/programmers/trainings/4/tree_height/



function solution(T) {
    return climbDownTheTree(T)
}

function climbDownTheTree(T) {

        if(!T){
            return -1
        }

        let leftSubtree = T.l
        let rightSubtree = T.r

        let left = climbDownTheTree(leftSubtree)
        let right= climbDownTheTree(rightSubtree)
  
  		return (right +1, left+1)

        
}

// Total score by Codility - 66%
