for i in {01..10}
do
	mkdir floor_$i
	for f in {01..10}
	do
		mkdir floor_$i/hall_$f
		for h in {01..10}
		do
			mkdir floor_$i/hall_$f/room_$h
			for s in {01..10}
			do
				touch floor_$i/hall_$f/room_$h/.shade_$s
			done
		done
	done
done
echo "McFriedChickenBucket">floor_04/hall_02/room_06/.shade_09