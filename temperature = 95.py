temperature = float(input("Enter Patient's current temperature: "))
if temperature >= 39:
    print("Patient is suspected of Covid-19. Require instant further investigation.")

elif temperature >= 38:
    print("Patient may be suffering from a fever. Require immediate biopsy.")
    

else:
    print("Patient's body temperature is normal.")