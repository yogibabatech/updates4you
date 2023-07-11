const toggle = () => {
    document.getElementById('nav').classList.toggle('navactive')
};


window.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".loaderweb").classList.add("loaderweb--hidden");
  });
window.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".loaderweb2").classList.add("loaderweb2--hidden");
  });


  
function loader2(){
    console.log("doing process")
    var loader1 = document.getElementById('loader2');
    console.log(loader1)
    loader1.classList.remove('loaderweb2--hidden');
    console.log(loader1)};



window.onload = function() {

    const rangeInput = document.querySelectorAll(".range-input input");
    priceInput = document.querySelectorAll(".price-input input");
    progress = document.querySelector(".slider .progress");
    
    let priceGap = 100;
    
    priceInput.forEach(input =>{
        input.addEventListener('input', e =>{
            let minValue =parseInt(priceInput[0].value);
            maxVal =  parseInt(priceInput[1].value);
            
            if(maxVal - minValue >= priceGap){
                if(e.target.className === "input-min"){
                    rangeInput[0].value = maxVal -priceGap;
                    prog = progress.style.left =  (minValue/rangeInput[0].max) * 100 + "%";
        
                }else{
                    rangeInput[1].value = minValue + priceGap;
                    prog = progress.style.right =  100 - (maxVal/rangeInput[1].max) * 100 + "%";
    
                }
            }
       
        });
    });
    
    
    
    rangeInput.forEach(input =>{
        input.addEventListener('input', e =>{
            let minValue = parseInt(rangeInput[0].value);
            maxVal = parseInt(rangeInput[1].value);
            
            if(maxVal - minValue < priceGap){
                if(e.target.className === "range-min"){
                    rangeInput[0].value = maxVal -priceGap;
                }else{
                    rangeInput[1].value = minValue + priceGap;
    
                }
    
            }else{
                priceInput[0].value = minValue;
                priceInput[1].value = maxVal;
                prog = progress.style.left = (minValue/rangeInput[0].max) * 100 + "%";
                prog = progress.style.right = 100 - (maxVal/rangeInput[1].max) * 100 + "%";
                console.log(prog)
    
            }
    
    
           
       
        });
    });
}
