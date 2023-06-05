# IRISAPI
Mini Project for IRIS API

- add, update, and delete from Demo.Person 

## NATIVE API
1. Install InterSystems IRIS Native API for Python, following the directions below for your operating system. Note that InterSystems Learning Labs, AWS, GCP, and Azure all use Linux.

- Windows: 
    ```  
    pip install nativeAPI_wheel\irisnative-1.0.0-cp34.cp35.cp36.cp37.cp38.cp39-none-win_amd64.whl 
    ```

- macOS: 
    ```  
    pip istall nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl
    ```
- Linux: 
    ```
    pip install nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl
    ```
## PYODBC (SQL)
2. Install InterSystems IRIS PyODBC drive
- Windows: 
  ```
  pyodbc_wheel\ODBC-2022.1.0.209.0-win_x64.exe
  ```
- macOS: 
  ```
  odbcinst –i –d –f pyodbc_wheel/mac/odbcinst.ini
  ```
- Linux: 
  ```
  sudo odbcinst -i -d -f pyodbc_wheel/linux/odbcinst.ini
  ```