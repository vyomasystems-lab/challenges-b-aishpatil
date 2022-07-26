# CTB Bugs for Level 1 Design 1

## Bugs

### 1. Select case for inp12 is Missing

> inp12 cannot be assigned to output as ```select case(5'b01100)``` is not present.
> Output will take default case value
> 
> <details>
>   <summary>Screenshots Here</summary>
>   
>   <p align="center">
>   <img src="https://user-images.githubusercontent.com/92450677/180609397-95d64efa-f65a-43ea-be6f-ba1684b3337d.png" />
>   </p>
>   
>   <p align="center">
>   <img src="https://user-images.githubusercontent.com/92450677/180632809-ee77de41-3523-4659-b803-aa83019b33a1.png" />
>   </p>
>   
>   </details>

### 2. Instead of inp13; inp12 assigned to out pin for 5'b01101

> Due to Bug 1, out pin is assigned with default case for 5'b01001. But when inp12 is assigned with random value zero then test case for inp12 will pass. 
> When select input is 5'b01101 then inp12 get assigned to output instead of inp13 due to same case for inp12 and inp13
> 
> <details>
>   <summary>Screenshots Here</summary>
>   
>   <p align="center">
>   <img src="https://user-images.githubusercontent.com/92450677/180633389-8255e4aa-98a8-46cf-a545-f6b0d8263035.png" />
>   </p>
>   
>   <p align="center">
>   <img src="https://user-images.githubusercontent.com/92450677/180633426-4a9d4c1b-5148-4174-9878-df136cc2e796.png" />
>   </p>
>   
>   </details>

### 3. Select case for inp30 is Missing

> inp30 cannot be assigned to output as ```select case(5'b11110)``` is not present. 
> Output will take default case value
> 
> <details>
>   <summary>Screenshots Here</summary>
>   
>   <p align="center">
>   <img src="https://user-images.githubusercontent.com/92450677/180633697-ce379c78-d91b-41f8-9f46-dfaa9982f51c.png" />
>   </p>
>   
>   </details>


## Result After Fixing All Bugs
> <details>
>   <summary>Screenshots Here</summary>
>   
>   <p align="center">
>   <img src="https://user-images.githubusercontent.com/92450677/180634058-58885e01-374c-4aef-ac8a-103ff4c3bf82.png" />
>   </p>
>   
>   </details>

