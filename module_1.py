import sys, operator

#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  f = open('suc_ph.csv', 'r')
  SUC = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if row[0] in SUC:
      SUC[row[0]] += 1
    else:
      SUC[row[0]] = 1
  f.close
  SUC_list = sorted(SUC.items(), key=operator.itemgetter(1), reverse = True)
  print "1. The region with the most SUC is " + SUC_list [0][0]

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  if school_year == '2010-2011':
    school_year = 2
  elif school_year == '2011-2012':
    school_year = 3
  elif school_year == '2012-2013':
    school_year = 4
    
  f = open('suc_ph.csv' , 'r')
  reg = {}
  for index, line in enumerate (f):
      row = line.split(',')
      #print row[2]
      if row[0] != 'region' and row[school_year] != '-':
        if row[0] in reg:
          reg[row[0]] += int(row[school_year])
        else:
          reg[row[0]] = int(row[school_year])
  #print suc
  f.close()
  reg_list = sorted(reg.items(), key = operator.itemgetter(1), reverse = True)
  print '2. The region with the most SUC enrollees is ' + reg_list[0][0]


#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  if school_year == '2009-2010':
    school_year = 5
  elif school_year == '2010-2011':
    school_year = 6
  elif school_year == '2011-2012':
    school_year = 7

  f = open('suc_ph.csv' , 'r')
  reg = {}
  for index, line in enumerate (f):
      row = line.split(',')
      if row[0] != 'region' and row[school_year].strip() != '-':
        if row[0] in reg:
          reg[row[0]] += int(row[school_year])
        else:
          reg[row[0]] = int(row[school_year])
  f.close()
  reg_list = sorted(reg.items(), key = operator.itemgetter(1), reverse = True)
  #print suc_list
  print "3. The region with the most SUC graduates is " + reg_list[0][0]

#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')

  if level ==  'BS' and school_year == '2010-2011':
    l_sy = 2
  elif level == 'BS' and school_year == '2011-2012':
    l_sy = 5
  elif level == 'BS' and school_year == '2012-2013':
    l_sy = 8

  SUC_TF = {}
  for index, line in enumerate (f):
      row = line.split(',')
      if row[l_sy] != 'first_sem_2010-2011_bs_ab' and row[l_sy] != 'first_sem_2011-2012_bs_ab' and row[l_sy] != 'first_sem_2012-2013_bs_ab' and row[l_sy] != '2500 regardless of the number of units' and row[l_sy] != '80 / 120' and row[l_sy] != '550/sem' and row[l_sy] != '50 / 100' and row[l_sy] != '-' and row[l_sy] != 'free tuition fee' and row[l_sy] != 'nds' and row[l_sy] != 'nd':
        if row[l_sy] == '142.5':
          SUC_TF[row[1]] = 142.5
        elif row[l_sy] == '158.8':
          SUC_TF[row[1]] = 158.8
        elif row[l_sy] == '125.5':
          SUC_TF[row[1]] = 125.5
        elif row[l_sy] == '133.1':
          SUC_TF[row[1]] = 133.1
        elif row[l_sy] == '145.5':
          SUC_TF[row[1]] = 145.5
        else: 
          SUC_TF[row[1]] = int(row[l_sy])
  f.close()
  SUC_list = sorted(SUC_TF.items(), key = operator.itemgetter(1))
  
  print "4. Top 3 cheapest SUC for " + level + " level in school year " + school_year
  print "  1. " + SUC_list [0][0]
  print "  2. " + SUC_list [1][0]
  print "  3. " + SUC_list [2][0]

  # for x in range(20):
  #   print SUC_list[x][0],SUC_list[x][1]

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')

  if level ==  'BS' and school_year == '2010-2011':
    l_sy = 2
  elif level == 'BS' and school_year == '2011-2012':
    l_sy = 5
  elif level == 'BS' and school_year == '2012-2013':
    l_sy = 8

  SUC_TF = {}
  for index, line in enumerate (f):
      row = line.split(',')
      if row[l_sy] != 'first_sem_2010-2011_bs_ab' and row[l_sy] != 'first_sem_2011-2012_bs_ab' and row[l_sy] != 'first_sem_2012-2013_bs_ab' and row[l_sy] != '2500 regardless of the number of units' and row[l_sy] != '80 / 120' and row[l_sy] != '550/sem' and row[l_sy] != '50 / 100' and row[l_sy] != '-' and row[l_sy] != 'free tuition fee' and row[l_sy] != 'nds' and row[l_sy] != 'nd':
        if row[l_sy] == '142.5':
          SUC_TF[row[1]] = 142.5
        elif row[l_sy] == '158.8':
          SUC_TF[row[1]] = 158.8
        elif row[l_sy] == '125.5':
          SUC_TF[row[1]] = 125.5
        elif row[l_sy] == '133.1':
          SUC_TF[row[1]] = 133.1
        elif row[l_sy] == '145.5':
          SUC_TF[row[1]] = 145.5
        else: 
          SUC_TF[row[1]] = int(row[l_sy])
  f.close()
  SUC_list = sorted(SUC_TF.items(), key = operator.itemgetter(1), reverse = True)
  
  print "5. Top 3 expensive SUC for " + level + " level in school year " + school_year
  print "  1. " + SUC_list [0][0]
  print "  2. " + SUC_list [1][0]
  print "  3. " + SUC_list [2][0]

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013 "BS"
def all_suc_who_have_increased_tuition_fee():
  l_sy1011 = 2
  l_sy1112 = 5
  l_sy1213 = 8

  suc_increase_TF = []
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  
  for index, line in enumerate (f):
    row = line.split(',')
    if row[l_sy1011] != 'first_sem_2010-2011_bs_ab' and row[l_sy1011] != 'first_sem_2011-2012_bs_ab' and row[l_sy1011] != 'first_sem_2012-2013_bs_ab' and row[l_sy1011] != '-' and row[l_sy1011] != 'free tuition fee' and row[l_sy1011] != 'nds' and row[l_sy1011] != 'nd' and row[l_sy1213] != 'first_sem_2010-2011_bs_ab' and row[l_sy1213] != 'first_sem_2011-2012_bs_ab' and row[l_sy1213] != 'first_sem_2012-2013_bs_ab' and row[l_sy1213] != '-' and row[l_sy1213] != 'free tuition fee' and row[l_sy1213] != 'nds' and row[l_sy1213] != 'nd': 
  		if row[l_sy1011] < row[l_sy1213]:
  			suc_increase_TF.append(row[1])

  f.close()
  suc = "\n ".join(suc_increase_TF)
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  print suc
#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
	
  f = open('performancesucprclicensureexam20102012.csv', 'r')

  print "7. The discipline which has the highest passing rate is"

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  if school_year == '2010' and discipline == 'Accountancy':
    syear = 3
  elif school_year == '2011' and discipline == 'Accountancy':
    syear = 4
  elif school_year == '2012' and discipline == 'Accountancy':
    syear = 5

  f = open('performancesucprclicensureexam20102012.csv' , 'r')
  suc_reg = {}
  for index, line in enumerate (f):
      row = line.split(',')
      if row[0] != 'region' and row[syear].strip() != '-' and row[2] == 'Accountancy':
        suc_reg[row[1]] = int(row[syear])
  f.close()
  suc_list = sorted(suc_reg.items(), key = operator.itemgetter(1),reverse=True)
  #for x in range(20):
    #print suc_list[x][0],suc_list[x][1]
  print "8. Top 3  SUC with highest passing rate in ",discipline," for school year 2010-",school_year
  print "  1. ",suc_list[0][0]
  print "  2. ",suc_list[1][0]
  print "  3. ",suc_list[2][0]
  #print "8. Top 3  SUC with highest passing rate in Accountancy for school year 2010-2011"
  #print "  1. Technological University of the Philippines"
  #print "  2. Marikina Polytechnic College"
  #print "  3. Apayao State College"



def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010-2011')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()