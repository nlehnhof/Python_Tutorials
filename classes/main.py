from pet import Pet
from dog import Dog

def main():
    randoPet = Pet("Mak", 12, "Shark", "blue")
    print(randoPet)

    d_o_g = Dog("Jake", 22, "Green", "German Shepherd")
    print(d_o_g)
    d_o_g.make_sound()

if __name__ == "__main__":
    main()