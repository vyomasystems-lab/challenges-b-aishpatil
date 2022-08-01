# CTB Bugs for Level 3 Design

### Bug 1 
> ```current_state = check_door``` <br>
> Until Door is not locked ```next_state``` must be check door <br>
> Due to bug at line 26, ```next_state``` is set as ```fill_water``` even though door is not closed <br>
>
> <details>
>  <summary>Screenshots Here</summary>
>  
>   > <details>
>   >  <summary>Bug Detected</summary>
>   >  
>   >  | | |
>   >  | :--: | :--: |
>   >  | Python Testcase | In Verilog Code |
>   >  | <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/182187228-2b30edfc-6fb9-4d63-b021-bee7ebf74c7c.png" /> | <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/182187482-c510ca89-119c-4cb2-98e2-ebf638d286d1.png"/> | 
>   >   
>   >  </details>
>   >  <details>
>   >  <summary>Bug Fixed </summary>
>   >  <br>
>   >  <p align="center"> <img src="https://user-images.githubusercontent.com/92450677/182192343-7d27189a-2a07-49fb-9162-dcdd55db296e.png" />
>   >
>   >  </details>
>  </details>



### Bug 2
> Door_locked before door Closed
>
> <details>
>   <summary>Screenshots Here</summary>
>   
>   <p align="center">
>   <img src="https://user-images.githubusercontent.com/92450677/182187620-12b91b77-9029-4d26-beb8-770678522512.png" />
>   </p>
>   
>   </details>

