import pandas as pd

class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def process_adoption(self):
        self.is_adopted = True
        print(f"✔ {self.name} has been successfully adopted!")

df_A = pd.read_csv("g_shelter_A.csv")
df_B = pd.read_csv("h_shelter_B.csv")

df = pd.concat([df_A, df_B], ignore_index=True)

df_clean = df.dropna()

dogs_df = df_clean[df_clean["Animal_Type"] == "Dog"]

print(dogs_df)


selected_dog = dogs_df[dogs_df["Pet_Name"] == "Sharlok"].iloc[0]
pet = RescuePet(
    name=selected_dog["Pet_Name"],
    species=selected_dog["Animal_Type"],
    age=selected_dog["Age_Years"]
)

pet.process_adoption()

adoption_record = pd.DataFrame([{
    "Pet_Name": pet.name,
    "Animal_Type": pet.species,
    "Age_Years": pet.age,
    "Adopted": pet.is_adopted
}])

adoption_record.to_csv(
    "j_Successful_adoptions.csv",
    mode="a",
    header=False,
    index=False
)

print("Adoption record saved to j_Successful_adoptions.csv")