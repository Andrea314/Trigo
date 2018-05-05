from math import sin, cos, asin, acos, degrees, radians, pi, sqrt


no=('\nTHERE ARE NOT ENOUGH NUMBERS TO DEFINE THE TRIANGLE\n')
dont=('\nTHIS TRIANGLE DOES NOT EXIST!\n')


class triangle:
	def __init__(self,a,b,c,alpha,beta,gamma):
		self.a=a
		self.b=b
		self.c=c
		self.alpha=alpha
		self.beta=beta
		self.gamma=gamma	

	def condition(self):
		a=self.a
		b=self.b
		c=self.c
		alfa=self.alpha
		beta=self.beta
		gamma=self.gamma	
		if alpha!=0 and beta!=0 and gamma!=0:
			x=alpha+beta+gamma
			if x!=0:
				print('\nthis triangle may not exist; check if alpha+beta+gamma is 180\n')

	def solution(self):
		a=self.a
		b=self.b
		c=self.c
		alpha=self.alpha
		beta=self.beta
		gamma=self.gamma
		while a==0 or b==0 or c==0 or alpha==0 or beta==0 or gamma==0:
			a1=a
			a2=a
			b1=b
			b2=b
			c1=c
			c2=c
			alpha1=alpha
			alpha2=alpha
			beta1=beta
			beta2=beta
			gamma1=gamma
			gamma2=gamma
			if alpha!=0 and beta!=0 and gamma!=0:
				pass
			else:
				if alpha!=0 and beta!=0:
					gamma=pi-alpha-beta
				if alpha!=0 and gamma!=0:
					beta=pi-alpha-gamma
				if beta!=0 and gamma!=0:
					alpha=pi-beta-gamma
			if b!=0 and alpha!=0 and beta!=0 and a==0:
				a=b*sin(alpha)/sin(beta)
			if c!=0 and alpha!=0 and gamma!=0 and a==0:
				a=c*sin(alpha)/sin(gamma)
			if a!=0 and alpha!=0 and beta!=0 and b==0:
				b=a*sin(beta)/sin(alpha)
			if c!=0 and beta!=0 and gamma!=0 and b==0:
				b=c*sin(beta)/sin(gamma)
			if a!=0 and alpha!=0 and gamma!=0 and c==0:
				c=a*sin(gamma)/sin(alpha)
			if b!=0 and beta!=0 and gamma!=0 and c==0:
				c=b*sin(gamma)/sin(beta)
			if a!=0 and b!=0 and beta!=0 and alpha==0:
				alpha=asin(a*sin(beta)/b)
			if a!=0 and c!=0 and gamma!=0 and alpha==0:
				alpha=asin(a*sin(gamma)/c)
			if a!=0 and b!=0 and alpha!=0 and beta==0:
				beta=asin(b*sin(alpha)/a)
			if b!=0 and c!=0 and gamma!=0 and beta==0:
				beta=asin(b*sin(gamma)/c)
			if a!=0 and c!=0 and alpha!=0 and gamma==0:
				gamma=asin(c*sin(alpha)/a)
			if b!=0 and c!=0 and beta!=0 and gamma==0:
				gamma=asin(c*sin(beta)/b)
			if b!=0 and c!=0 and alpha!=0 and a==0:
				a=sqrt((b**2)+(c**2)-2*b*c*cos(alpha))
			if b!=0 and c!=0 and gamma!=0 and a==0:
				a=sqrt((b**2)-(c**2)+2*a*b*cos(gamma))
			if b!=0 and c!=0 and beta!=0 and a==0:
				a=sqrt((b**2)-(c**2)+2*a*c*cos(beta))
			if a!=0 and c!=0 and beta!=0 and b==0:
				b=sqrt((a**2)+(c**2)-2*a*c*cos(beta))
			if a!=0 and c!=0 and gamma!=0 and b==0:
				b=sqrt((a**2)-(c**2)+2*a*b*cos(gamma))
			if a!=0 and c!=0 and alpha!=0 and b==0:
				b=sqrt((a**2)-(c**2)+2*b*c*cos(alpha))
			if a!=0 and b!=0 and gamma!=0 and c==0:
				c=sqrt((a**2)+(b**2)-2*a*b*cos(gamma))
			if a!=0 and b!=0 and beta!=0 and c==0:
				c=sqrt((a**2)-(b**2)+2*a*c*cos(beta))
			if a!=0 and b!=0 and alpha!=0 and c==0:
				c=sqrt((a**2)-(b**2)+2*b*c*cos(alpha))
			if a!=0 and b!=0 and c!=0 and alpha==0:
				alpha=acos((b**2+c**2-a**2)/(2*b*c))
			if a!=0 and b!=0 and c!=0 and beta==0:
				beta=acos((a**2+c**2-b**2)/(2*a*c))
			if a!=0 and b!=0 and c!=0 and gamma==0:
				gamma=acos((a**2+b**2-c**2)/(2*a*b))
			if a==a1 and b==b1 and c==c1 and alpha==alpha1 and beta==beta1 and gamma==gamma1:
				print(no)
				a=1 
				b=1 
				c=1 
				alpha=pi
				beta=pi 
				gamma=pi

		if a+b<=c and a+c<=b and b+c<=a:
			print(dont)
		if a==1 and b==1 and c==1 and alpha==1 and beta==1 and gamma==1:
			print(dont)
		else:
			if alpha+beta+gamma!=pi:
				print(no)
			perimeter=a+b+c
			area=0.5*a*b*sin(gamma)
			alpha=degrees(alpha)
			beta=degrees(beta)
			gamma=degrees(gamma)
			a='{0:.5f}'.format(a)
			b='{0:.5f}'.format(b)
			c='{0:.5f}'.format(c)
			alpha='{0:.5f}'.format(alpha)
			beta='{0:.5f}'.format(beta)
			gamma='{0:.5f}'.format(gamma)
			perimeter='{0:.5f}'.format(perimeter)
			area='{0:.5f}'.format(area)
			print('\n\nSOLUTION:\n\na         = ',a,'\nb         = ',b,'\nc         = ',c,'\nalpha     = ',alpha,'\nbeta      = ',beta,'\ngamma     = ',gamma,'\nperimeter = ',perimeter,'\narea      = ',area,'\n\n\n')



print('TRIGO BY ANDREA314\n\n')
print("Insert the numbers; if you do not know the number insert 0\nInsert the angle numbers in degrees\n\na = angle alpha opposite side\nb = angle beta opposite side\nc = angle gamma opposite side\n\n\n")
while True:
	lista=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z','a1','b1','c1','d1','e1','f1','g1','h1','i1','j1','k1','l1','m1','n1','o1','p1','q1','r1','s1','t1','u1','v1','x1','y1','w1','z1''a2','b2','c2','d2','e2','f2','g2','h2','i2','j2','k2','l2','m2','n2','o2','p2','q2','r2','s2','t2','u2','v2','x2','y2','w2','z2']
	a=float(input('a     = '))
	b=float(input('b     = '))
	c=float(input('c     = '))
	alpha=float(input('alpha = '))
	beta=float(input('beta  = '))
	gamma=float(input('gamma = '))
	print(' ')
	alpha=radians(alpha)
	beta=radians(beta)
	gamma=radians(gamma)
	if a==0 and b==0 and c==0 and alpha==0 and beta==0 and gamma==0:
		print(no)
	if a==0 and b==0 and c==0:
		print(no)
	if a==0 and b==0 and c==0 and alpha==0 and beta==0:
		print(no)
	if a==0 and b==0 and c==0 and alpha==0 and gamma==0:
		print(no)
	if a==0 and b==0 and c==0 and beta==0 and gamma==0:
		print(no)
	if a==0 and b==0 and alpha==0 and beta==0 and gamma==0:
		print(no)
	if a==0 and c==0 and alpha==0 and beta==0 and gamma==0:
		print(no)
	if b==0 and c==0 and alpha==0 and beta==0 and gamma==0:
		print(no)
	if a==0 and b==0 and c==0 and alpha==0:
		print(no)
	if a==0 and b==0 and c==0 and gamma==0:
		print(no)
	if a==0 and b==0 and c==0 and beta==0:
		print(no)
	else:
		if a!=0 and b!=0 and c!=0:
			amb=a+b
			amc=a+c
			bmc=c+c
			if a>bmc or b>amc or c>amb:
				print('THIS TRIANGLE DOES NOT EXIST!')
				break
		lista[0]=triangle(a,b,c,alpha,beta,gamma)
		lista[0].condition()
		lista[0].solution()
		del lista[0]
