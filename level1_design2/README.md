# CTB Bugs for Level 1 Design 2

## Bugs

### 1. SEQ_1011

> After detecting 1st sequence pattern 1011, ```next_state``` changes to `IDLE` instead of SEQ_1 for bit 1 or SEQ_10 for bit 0 <br>
> This prevents overlapping sequences from being successfully identified. 
> <details>
>  <summary>Screenshots Here</summary>
>  
>   > <details>
>   >  <summary>Bug Detected</summary>
>   >  
>   >  | | |
>   >  | :--: | :--: |
>   >  | Python Testcase | In Verilog Code |
>   >  | <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181771627-32e1412f-1e37-4437-8acc-c471a998c9db.png" /> | <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181771796-cfb0c820-fb1a-4cca-b1a8-572e0a4ec61b.png"/> | 
>   >   
>   >  </details>
>   >  <details>
>   >  <summary>Bug Fixed </summary>
>   >  <br>
>   >  <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181775188-b50d679b-eddb-4459-a1ad-9c160be99e63.png" />
>   >
>   >  </details>
>  </details>


### 2. SEQ_101

> After detecting sequence pattern 101, ```next_state``` changes to `IDLE` instead of SEQ_10 for bit 0  <br> <br>
> This prevents overlapping sequences from being successfully identified. 
> <details>
>  <summary>Screenshots Here</summary>
>  
>   > <details>
>   >  <summary>Bug Detected</summary>
>   >  
>   >  | | |
>   >  | :--: | :--: |
>   >  | Python Testcase | In Verilog Code |
>   >  | <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181866076-f3258693-3a7d-4f4c-8472-79aac4a9d0c2.png" /> | <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181865837-1dcfd7da-2fde-4870-8e0e-5b22274aa6d3.png"/> | 
>   >   
>   >  </details>
>   >  <details>
>   >  <summary>Bug Fixed </summary>
>   >  <br>
>   >  <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181865871-4b3247d4-aa91-4e80-a181-561718b18686.png" />
>   >
>   >  </details>
>  </details>


### 3. SEQ_1

> After detecting sequence pattern 1, ```next_state``` changes to `IDLE` instead of SEQ_1 for bit 1 <br>
> This prevents overlapping sequences from being successfully identified.
> <details>
>  <summary>Screenshots Here</summary>
>  
>   > <details>
>   >  <summary>Bug Detected</summary>
>   >  
>   >  | | |
>   >  | :--: | :--: |
>   >  | Python Testcase | In Verilog Code |
>   >  | <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181866280-3c5b01d8-06ce-4863-864b-5a24ba209ff7.png" /> | <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181866308-5eba2a10-5adc-4b3d-a3ce-212ac35c9e0d.png"/> | 
>   >   
>   >  </details>
>   >  <details>
>   >  <summary>Bug Fixed </summary>
>   >  <br>
>   >  <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/181866326-4c33340f-c253-4b89-9315-e1c6987bc69d.png" />
>   >
>   >  </details>
>  </details>
