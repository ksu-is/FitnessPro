
print('Welcome to Fitness Pro, exercise guide where you will be asked various questions to help us provide you wil the most comprehensive and personalized workout.')

#General exercises
Yoga = ['chair','cresent lunge', 'half Moon', 'warrior two', 'eagle', 'standing foot to head', 'bird of paradise', 'extended side angle' ]
Stretching = ['lunge with spiral twist','foward fold', 'half split', 'figure four', '90/90', 'lunging hip flexor', 'reclined spinal twist' ]

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
            target_body = input('Please choose upperbody or lowerbody: ')
            if target_body.lower() == 'upperbody':
                
                area_p = input('Choose which area: ')
                if area_p.lower() == 'arm' or 'arms':
                    print(arm_e, '10 - 12 times each exercise, 4 sets')
                elif area_p.lower() == 'shoulder' or 'shoulders':
                    print(shoulder_e, '10 - 12 times exercise, 4 sets')
                elif area_p.lower() == 'back':
                    print(back_e, '10 - 15 times each exercise, 4 sets')
                elif area_p.lower() == 'abs':
                    print(abs_e, '10 - 12 times each exercise, 4 sets')

            elif target_body.lower() == 'lowerbody':
                area_p = input('Choose which area:')
                if area_p.lower() == 'leg' or 'legs':
                    print(leg_e, '12 - 18 times each exercise, 4 sets')
                elif area_p.lower() == 'glutes':
                    print(glutes_e, '15 - 18 times each exercise, 4 sets')
        elif equipment.lower() == 'no':
            workout_time += 1
            target_body = input('Please choose upperbody or lowerbody: ')
            if target_body.lower() == 'upperbody':
                area_p = input('Choose which area: ')
                if area_p.lower() == 'arm'or 'arms':
                    print(arm_ne, ' 12 - 15 times each exercise, 4 sets')
                elif area_p.lower() == 'shoulder' or 'shoulders':
                    print(shoulder_ne, '12 - 15 times each exercise, 4 sets')
                elif area_p.lower() == 'back':
                    print(back_ne, ' 12 - 15 times each exercise, 5 sets')
                elif area_p.lower() == 'abs':
                    print(abs_ne, ' 13 - 16 times each exercise, 4 sets')
            elif target_body.lower() == 'lowerbody':
                area_p = input('Choose which area: ')
                
                if area_p.lower() == 'leg' or 'legs':
                    print(leg_ne +' 15 - 20 times each exercise, 5 sets')
                    
                elif area_p.lower() == 'glutes':
                    print(glutes_ne, ' 15 - 18 times each exercise, 4 sets') 
fitness_guide()
