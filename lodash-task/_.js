//This file is my code

const _ = {

    clamp(number,lower,upper){

        /*
            if(number < lower){
                return lower;
            }else if(number > upper){
                return upper;
            }else{
                return number;
            }
        */
       //return Math.min(Math.max(number,lower),upper);
    },

    inRange(number,start,end){

        if(end===undefined){
            end = start;
            start = 0;
        }
        if(start > end){
            let temp = start;
            start = end;
            end = temp;
        }
        //console.log(`is ${number} between ${start} and ${end} inclusive?`)
        return (number >= start && number < end) ? true : false;
    },

    words(string){

        return string.split(' ');

    },

    pad(string,length){

        while(string.length<length){

            let dif = length - string.length;

            if(dif >= 2){
                string = ` ${string} `
            } 
            else if (dif = 1)   
            {
                string = `${string} `
            }
            
        }
        return string;
    },

    has(obj,key){

        let val = obj[key]

        return (val === undefined) ? false : true;

    },

    invert(obj){
        
        const newObj = {}

        for(const [key,value] of Object.entries(obj)){

            newObj[value] = key
        }

        return newObj;
    },

    findKey(obj,func){

        for(const[key,value] of Object.entries(obj)){

            if(func(value)){
                return key;
            }
        }
        return undefined;

    },
    
    drop(arr,num=1){

        for(let i = num;i>0;i--){
            arr.shift()
        }
        return arr;

    },

    dropWhile(arr,func){
        
        for(let i = 0;i<arr.length;i++){

            if(!func(arr[i],i,arr))
            {                
                return this.drop(arr,i);
            }


        }
    },

    chunk(arr,size=1){

        let newArr = []

        for(let i = 0;i < arr.length;i+=size){
            
            newArr.push(arr.slice(i,i+size))

        }

        return newArr;
    }
};




// Do not write or modify code below this line.
module.exports = _;