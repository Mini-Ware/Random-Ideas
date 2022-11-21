import shelve

try:
    db = shelve.open("database")
    db.clear()

    #create and update
    db["amogus"] = "sussy"
    db.update({"red":"sus"})
    db.update({"blue":"not sus"})
    db.update({"imposter":"red"})

    #read
    print(db.get("amogus"))

    #retrieve all
    print(list(db.keys()))
    print(list(db.values()))

    #delete
    db.pop("blue")
    print(list(db.items()))

    #checking values
    print("amog" in db)
    print("amogus" in db)
except ValueError:
    print("Code given invalid values!")
except ZeroDivisionError:
    print("Code tried to divide by zero!")
except IOError:
    print("Code has file related error!")
except:
    print("Code has unknown error!")
else:
    print("Code has no errors! :D")
finally:
    print("Closing file...")
    db.close()
