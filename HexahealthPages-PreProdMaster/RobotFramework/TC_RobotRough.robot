*** Test Cases ***

Library Requestslibrary

*** Variables ***
${base_url}   https://dummy.restapiexample.com/api/v1/employees
${id}  12

Get_weatherinfo
	create session mysession ${base_url}
	${response} =  get request mysession

