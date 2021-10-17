'use strict';

document.addEventListener('DOMContentLoaded', () =>{
    const blocks = document.querySelectorAll('.item');
    const winner = document.querySelector('.winner');

    const arr = [];
    let i = 0;

    for(let j = 0; j < 9; j++)
        arr[j] = 0;


    let Test = function(q) {
        let checkPos = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3 ,4 ,5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
        // console.log("------------------------------")
        let message = ""
        let combination = []
        checkPos.forEach((pos) => {
            // console.log("TU", arr[pos[0]], arr[pos[1]], arr[pos[2]]);
            if(arr[pos[0]] == q && arr[pos[1]] == q && arr[pos[2]] == q){
                if(q == 1){
                    message = "Winner crosses";
                    combination = pos;
                }
                else{
                    message = "Winner zeros";
                    combination = pos;
                }
            }
        })

        // if((arr[0] == q && arr[3] == q && arr[6] == q) || ((arr[1] == q && arr[4] == q && arr[7] == q)) || ((arr[2] == q && arr[5] == q && arr[8] == q)) || ((arr[0] == q && arr[1] == q && arr[2] == q)) || ((arr[3] == q && arr[4] == q && arr[5] == q)) || ((arr[6] == q && arr[7] == q && arr[8] == q)) || ((arr[0] == q && arr[4] == q && arr[8] == q)) || ((arr[2] == q && arr[4] == q && arr[6] == q)))
        // {
        //     if(q == 1){
        //         return "Winner crosses";
        //     }
        //     else{
        //         return "Winner zeros";
        //     }
        // }

        let check = true
        arr.forEach((item) => {
            if(item != 1 && item != 2){
                check = false
            }
        })

        if(check){
            message = "Draw";
        }

        return [message, combination]    
    };

    function checkWinner(){
        let ans = Test(1);

        if(ans[0] == ""){
            ans = Test(2)
        }

        if(ans[0]){
            alertMessage(ans[0], ans[1]);
        }
    }

    const alertMessage = function(message, items) {
        winner.textContent = message;
        items.forEach((i) => {
            blocks[i].style.backgroundColor = "blue";
        })

        for(let i = 0; i < 9; i++){
            if(arr[i] != 1 && arr[i] != 2){
                blocks[i].innerHTML = `
                    <div class="item">
                        ---
                    </div>
                `;
            }
        }
        arr.forEach((item) => {
            if(item != 1 && item != 2){
                check = false
            }
        })
    }

    const write = function(e, index){
        e.addEventListener('click', (event) =>{
            event.preventDefault();
            if(!e.textContent)
            {
                if(i % 2 == 0){
                    e.innerHTML = `
                    <div class="item">
                        &times
                    </div>
                    `;

                    arr[index] = 1;
                }
                else{
                    e.innerHTML = `
                    <div class="item">
                        &#9675
                    </div>
                    `;
                    arr[index] = 2;
                }
                i++;
            }
            checkWinner();
        });
    };

    blocks.forEach(function (block, index){
        write(block, index);
    });
});