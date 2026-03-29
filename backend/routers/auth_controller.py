""" from fastapi import APIRouter

auth_controller = APIRouter()

# Rutas relacionadas con la autenticacion
@auth_controller.post("/auth/login")
async def login():
    return {"message": "Login successful"}

@auth_controller.post("/auth/signup")
async def signup():
    return {"message": "Signup successful"}

@auth_controller.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = ""
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña es incorrecta")
    
    access_token = create_access_token(data={"sub": user.username}) """