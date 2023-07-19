
//https://app.codility.com/programmers/trainings/4/first_unique/


function isNumber(element){
    return typeof element === 'number'
}
function solution(A) {
    if(A.length>0 && A.every(isNumber)){
        let repeatingValues = A.filter((element, index) => A.indexOf(element) !== index)

       let uniqueValues =  A.filter(element=> !repeatingValues.includes(element))
       if(uniqueValues.length === 0 ){
           return -1
       } return uniqueValues[0]
    }
}

//Total score by Codility = 72%