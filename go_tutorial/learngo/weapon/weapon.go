package weapon

/*
	Pay attention to lower case and upper case.
	Undercase names are private to this module.
	Uppercase names are exported.

	In main, we can access the weapon's Name, New(), and Attack(). All other attributes are not exported.
*/

import "math/rand"

type weapon struct {
	Name       string
	weaponType string
	damage     float64
	reach      float64
	weight     float64
}

func New(name string, weaponType string, damage float64, reach float64, weight float64) weapon {
	weapon := weapon{name, weaponType, damage, reach, weight}
	return weapon
}

func (w weapon) Attack() float64 {
	r1 := rand.Float64()
	damage := r1 * w.damage
	return damage
}
