package armor

import "fmt"

type armorstats struct {
	Defense float64
	Weight  float64
}

type Armor struct { // I am pretending like Armor is really armor, it just made things a bit easier
	Name       string
	armorstats // see how we reference another struct - this is somewhat like inheritence
}

type ArmorInventory struct {
	Armors []Armor
}

func NewArmorStats(defense float64, weight float64) armorstats {
	stats := armorstats{defense, weight}
	return stats
}

func NewArmor(name string, stats armorstats) Armor {
	arm := Armor{name, stats}
	return arm
}

func (a Armor) PrintInfo() {
	fmt.Printf("%s has %f Defense and is %f lbs.\n", a.Name, a.Defense, a.Weight) // notice how we refer to the reference struct as if it was a primary property
}

func (a ArmorInventory) PrintArmorNames() {
	for _, v := range a.Armors {
		fmt.Println(v.Name)
	}
}
