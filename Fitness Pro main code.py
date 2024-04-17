print('Welcome to Fitness Pro, exercise guide where you will be asked various questions to help us provide you wil the most comprehensive and personalized workout.')

# No equitment: Women exercises 
yoga_w = ['chair','cresent lunge', 'half Moon', 'warrior two', 'eagle', 'standing foot to head', 'bird of paradise', 'extended side angle' ]
stretching_w = ['lunge with spiral twist','foward fold', 'half split', 'figure four', '90/90', 'lunging hip flexor', 'reclined spinal twist' ]

# No equitment: Men exercises 
stretching_m = ['Hamstring hinge stretch','overhead reach stretch', 'diagonal reach stretch', 'calf stretch', 'side lunge stretch', 'glute stretch','standing quad stretch', 'chest stretch']
Bodyweightexercises_m = ['pushup','plank', 'glute bridge', 'burpee', 'close grip pushup', 'pike pushup','bodyweight squat', 'diamond pushup']
# Women Exercises
arm_w = ['biceps curls', 'cactus arms', 'upright row', 'lying overhead tricep extension', 'tricep kickback', 'Curtsey lunge with bicep curl', 'Rear delt fly', 'triceps dip']
leg_w = ['hip circles', 'jump rope', 'skaters', 'walking lunges', 'donkey kicks', 'broad jumps', 'goblet squat', 'Rear delt fly', 'squat with heal raise']
abs_w = ['glute bridge march', 'mountain climbers', 'plank with knee tap', 'should tap and jack', 'leg lower', 'dead bug', 'v up', 'hollow body hold']

# Men exercises
arm_m = ['bicep curl', 'incline tricep extension', 'strict press', 'hammer curl', 'overhead tricep extension', 'lateral rasises', 'bent over row', 'skullcrusher']
leg_m = ['barbell back squat', 'barbell dead lift', 'front squat', 'kettlebell swing', 'walking lunge', 'lateral lunge', 'goblet squat', 'bulgarian split squat' ]
abs_m = [ 'plank hold', 'half kneeling kettlebell windmill', 'hanging leg raise', 'russian twist', 'copenhagan plank', 'cable crunch', 'pallof press', 'ball slams']


def fitness_guide():
    workout_time = 0
    equipment = input('Please enter yes or no for equipment: ')
    while workout_time <2:
        if equipment.lower() == 'yes':
            workout_time += 1
            gender_body = input('Please choose female or male: ')
            if gender_body.lower() == 'female':
                area_p = input('Choose which area: ')
                if area_p.lower() == 'arm' or 'arms':
                    print(arm_w, '10 - 12 times each exercise, 4 sets')
                elif area_p.lower() == 'shoulder' or 'shoulders':
                    print(leg_w, '10 - 12 times exercise, 4 sets')
                elif area_p.lower() == 'back':
                    print(abs_w, '10 - 15 times each exercise, 4 sets')

            elif gender_body.lower() == 'male':
                area_p = input('Choose which area:')
                if area_p.lower() == 'arm' or 'arms':
                    print(arm_m, '12 - 18 times each exercise, 4 sets')
                elif area_p.lower() == 'leg' or 'legs':
                    print(leg_m, '15 - 18 times each exercise, 4 sets')
                elif area_p.lower() == 'ab' or 'abs':
                    print(abs_m, '15 - 18 times each exercise, 4 sets')
        elif equipment.lower() == 'no':
            workout_time += 1
            gender_body = input('Please choose female or male: ')
            if gender_body.lower() == 'female':
                area_p = input('Choose which area: yoga or stretching ')
                if area_p.lower() == 'yoga':
                    print(yoga_w, ' 12 - 15 times each exercise, 4 sets')
                elif area_p.lower() == 'stretch' or 'stretching':
                    print(stretching_w, '12 - 15 times each exercise, 4 sets')
                elif gender_body.lower() == 'male':
                    area_p = input('Choose which area: stretching or bodyweight')
                if area_p.lower() == 'stretch' or 'stretching':
                    print(stretching_m +' 15 - 20 times each exercise, 5 sets')
                elif area_p.lower() == 'bodyweight':
                    print(Bodyweightexercises_m, ' 15 - 18 times each exercise, 4 sets') 
fitness_guide()