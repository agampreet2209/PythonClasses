# dictionary ->  its an ordered collection with key-value pair. In it duplicacy not allowed

trip = {
	"location": "Goa",
	"Budget": 25000,
	"members": 4,
	"nod": 6
}

trip["Budget"] = 40000
trip["ModeOfTransportation"] = "By Air"
trip.pop("nod")

print(trip)
print(trip["location"])

for key in trip:
	print(key,":",trip[key])

for key, value in trip.items():
	print(key,":",value)