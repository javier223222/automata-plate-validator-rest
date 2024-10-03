from fastapi import APIRouter,UploadFile,File,HTTPException
from fastapi.responses import FileResponse
from app.core.services import validate_plate
from app.adapters.file_adapter import read_file
import pandas as pd
import os



router = APIRouter()
@router.post("/validate_plate")
async def validate_plate_from_file(file: UploadFile = File(...)):
    
    try:
        patterns=read_file(file)

        
     
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    results = []
    if isinstance(patterns, pd.DataFrame):
       
        
        
        for row_index,row in patterns.iterrows():
            for col_index,value in enumerate(row):
                textevaluate=str(value)
                textevaluate=textevaluate.split()
                for text in textevaluate:
                  if validate_plate(str(text)):
                     results.append({
                        "fila": row_index + 1,
                        "columna": col_index + 1,
                        "texto": value,
                     })
    else:
        
        for index,line in enumerate(patterns):
            posible_plate = line.split()
            
            for plate in posible_plate:
                if validate_plate(str(plate)):
                    
                    position=get_position(line,plate)

                   
                    
                    results.append({
                        "fila": index + 1,
                        "columna": 1,
                        "texto": str(plate),
                        "posicion": position + 1,
                    })
                    
    output_file = os.path.join(os.path.expanduser("~"), "results.csv")

    if results:
        write_results_to_csv(results, output_file)
        return FileResponse(output_file, media_type="text/csv", filename="results.csv")
    else :
        return {"message":"No se encontraron patrones validos en el archivo"}



# funcion para escibir el resultado en un  archivo
def write_results_to_csv(results, output_file):
    
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)

# funcion para obtener la posicion de la cadena dentro del archivo
def get_position(line, plate_text):
    return line.index(plate_text)
  