
print('Welcome to your Fitness Guide!')


arm_ne = ['arms circle', 'tricep dips', 'push-ups', 'body saw']
back_ne = ['superman','plank', 'reverse snow angels', 'aquaman' ]
shoulder_ne = ['plank tap', 'side plank with lateral raise', 'crab walk', 'incline push-up'  ]
abs_ne = ['mountain climber twist', 'plank up', 'bicycle crunch', 'reverse crunch']

arm_e = ['biceps curls', 'triceps kickback', 'overhead extension', 'ches press']
shoulder_e = ['dumbell side raises', 'dumbbell shoulder press', ' dumbell front raise', 'bent over side raises']
back_e = ['Dumbbell Upright Row', 'Dumbbell Renegade Row', 'Alternating Bent-Over Row', 'Kneeling One Arm Row']
abs_e = ['swing', 'side bend', 'russian twist', 'wood chop']


leg_ne = 'side lunges' + '\n' + 'curtsy lunges' +  '\n' + 'side leg raises each leg' +  '\n'+ 'bodyweight squats' +  '\n' +  'Bulgarian Split Squats'
glutes_ne = ['zumo squats', 'glute bridge', 'reverse lunge', 'jumping lunge', 'jump squat' ]

leg_e = [ 'dumbell lunge', 'dumbell side lunge', 'dumbell deadlift', 'dumbell cald raises', 'goblet squat']
glutes_e = [ 'dumbell Squat to Lateral Leg Lift', 'dumbell sumo squat', 'weighted glute bridge', 'weighted donkey kick']


lower_cardio = [ 'high knees', 'side to side shuffle', 'jumping squat,', 'squat knee to elbow']
upper_cardio = [ 'shadowboxing,', 'mountain climbers', 'jumpink jacks', 'burpees' ]


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
