clear all
close all

format short

%% Exercise 1

%Set 1
a1=[0 0 0];
a2=[3 7 1];
a3=[5 1 3];
b=3;
c=4;
d=5;


%Set 2
%a1=[1 -1 0];
%a2=[5 8 4];
%a3=[7 3 1];
 
%b=7;
%c=6;
%d=4;

% a) function analysed at x_0
syms x y z
f1=sqrt((x-a1(1))^2+(y-a1(2))^2+(z-a1(3))^2)-b;
f2=sqrt((x-a2(1))^2+(y-a2(2))^2+(z-a2(3))^2)-c;
f3=sqrt((x-a3(1))^2+(y-a3(2))^2+(z-a3(3))^2)-d;

f1smart=(x-a1(1))^2+(y-a1(2))^2+(z-a1(3))^2-b^2;
f2smart=(x-a2(1))^2+(y-a2(2))^2+(z-a2(3))^2-c^2;
f3smart=(x-a3(1))^2+(y-a3(2))^2+(z-a3(3))^2-d^2;

fx0=double(subs([f1,f2,f3],[x,y,z],[1,1,1]))
fx0smart=double(subs([f1smart,f2smart,f3smart],[x,y,z],[1,1,1]))

% b) Jacobian analysed at x_0
jacob=[[diff(f1,x),diff(f1,y),diff(f1,z)],
    [diff(f2,x),diff(f2,y),diff(f2,z)],
    [diff(f3,x),diff(f3,y),diff(f3,z)]]
jacobsmart=[[diff(f1smart,x),diff(f1smart,y),diff(f1smart,z)],
    [diff(f2smart,x),diff(f2smart,y),diff(f2smart,z)],
    [diff(f3smart,x),diff(f3smart,y),diff(f3smart,z)]]

Dfx0=double(subs(jacob,[x,y,z],[1,1,1]))
Dfx0smart=double(subs(jacobsmart,[x,y,z],[1,1,1]))

% c) LU factorization
P=reshape([1,0,0,0,1,0,0,0,1],[3,3])
%P=reshape([0,0,1,0,1,0,1,0,0],[3,3])

% Doolittle
PDfx0= P*Dfx0
PDfx0smart=P*Dfx0smart
[L,U]=doolittle(PDfx0);
double(L)
double(U)
[Lsmart,Usmart]=doolittle(PDfx0smart);
Lsmart
Usmart
%%

%Crouts
PDfx0=P*Dfx0
PDfx0smart=P*Dfx0smart
[LC,UC]=LU_Crout(PDfx0);
double(LC)
double(UC)
[LCsmart,UCsmart]=LU_Crout(PDfx0smart);
double(LCsmart)
double(UCsmart)

%inverse
inv(PDfx0)
inv(PDfx0smart)



% for Broyden 1 - solve linear system
%Crouts
y=LC\fx0'
UC\y
ysmart=LCsmart\fx0smart'
UCsmart\ysmart


A=double(PDfx0)
B=double(inv(PDfx0))

double(cond(PDfx0,Inf))


% e) Broyden method
f=@(x) [sqrt((x(1)-a1(1))^2+(x(2)-a1(2))^2+(x(3)-a1(3))^2)-b;sqrt((x(1)-a2(1))^2+(x(2)-a2(2))^2+(x(3)-a2(3))^2)-c;sqrt((x(1)-a3(1))^2+(x(2)-a3(2))^2+(x(3)-a3(3))^2)-d]

% Broyden 1
broyden1(f,[1;1;1],A,2)

%Broyden 2
broyden2(f,[1;1;1],B,2)


%% Exercise 2

% example from the net: https://www.colorado.edu/amath/sites/default/files/attached-files/fredholm.pdf
% xp=[0,pi/4,pi/2]
% h=pi/4
% syms x t
% f=@(x) sin(x)
% K=@(x,t) (sin(x)*cos(t))
% L=@(x,t) 1
% lambda=1
% mu=0
% phiexact=@(x) 2*sin(x)

% Version 1, 2
% xp=[0,pi/2,pi]
% h=pi/2
% syms x t
% f=@(x) pi*x^2
% K=@(x,t) (0.5*sin(3*x)-t*x^2)
% L=@(x,t) 1
% lambda=3
% mu=0
% phiexact=@(x) -0.5*sin(3*x)

% Version 3, 4
xp=[0,1,2]
h=1
syms x t
f=@(x) 2*cos(x)-x*cos(2)-2*x*sin(2)+x-1
K=@(x,t) x*t
L=@(x,t) x-t
lambda=1
mu=1
phiexact=@(x) cos(x)

btrap=[-f(xp(1));-f(xp(2));-f(xp(3))]
Atrap=[[lambda*h/2*K(xp(1),xp(1))-1, lambda*h*K(xp(1),xp(2)),lambda*h/2*K(xp(1),xp(3))];
    [lambda*h/2*K(xp(2),xp(1))+mu*h/2*L(xp(2),xp(1)),lambda*h*K(xp(2),xp(2))+mu*h/2*L(xp(2),xp(2))-1,lambda*h/2*K(xp(2),xp(3))];
    [lambda*h/2*K(xp(3),xp(1))+mu*h/2*L(xp(3),xp(1)),lambda*h*K(xp(3),xp(2))+mu*h*L(xp(3),xp(2)),lambda*h/2*K(xp(3),xp(2))+mu*h/2*L(xp(3),xp(2))-1]]
yptrap=Atrap\btrap

bsimp=[-f(xp(1));-f(xp(2));-f(xp(3))]
Asimp=[[lambda*h/3*K(xp(1),xp(1))-1, lambda*4*h/3*K(xp(1),xp(2)),lambda*h/3*K(xp(1),xp(3))];
    [lambda*h/3*K(xp(2),xp(1))+mu*h/2*L(xp(2),xp(1)),lambda*4*h/3*K(xp(2),xp(2))+mu*h/2*L(xp(2),xp(2))-1,lambda*h/3*K(xp(2),xp(3))];
    [lambda*h/3*K(xp(3),xp(1))+mu*h/3*L(xp(3),xp(1)),lambda*4*h/3*K(xp(3),xp(2))+mu*4*h/3*L(xp(3),xp(2)),lambda*h/3*K(xp(3),xp(2))+mu*h/3*L(xp(3),xp(2))-1]]
ypsimp=Asimp\bsimp

figure
plot(xp,yptrap,'o')
hold on
plot(xp,ypsimp,'o')
plot(xp,phiexact(xp),'x')
hold off

function x=broyden1(f,x0,a,k)
 
  for i=1:k
    inva = inv(a)
    f(x0)
    x=x0-inva*f(x0) 
    del=x-x0
    f(x)
    delta=f(x)-f(x0)
    a=a+(delta-a*del)*del'/(del'*del)
    x0=x;
  end
end

function x=broyden2(f,x0,b,k)
  for i=1:k
    x=x0-b*f(x0) 
    del=x-x0
    delta=f(x)-f(x0)
    b=b+(del-b*delta)*del'*b/(del'*b*delta)
    x0=x;
  end
end

function [L U]=LU_Crout(A)
%Function to carryout LU factorization using Crout's Algorithm
%By Mazhar Iqbal,NUST College of E&ME,Islamabad,Pakistan
m=length(A);
L=zeros(size(A));
U=zeros(size(A));
L(:,1)=A(:,1);
U(1,:)=A(1,:)/L(1,1);
U(1,1)=1;
for k=2:m
for j=2:m
    for i=j:m
        L(i,j)=A(i,j)-dot(L(i,1:j-1),U(1:j-1,j));
    end
    U(k,j)=(A(k,j)-dot(L(k,1:k-1),U(1:k-1,j)))/L(k,k);
end
end
end

function [L U] = doolittle(A)
[m,n]=size(A);
U=zeros(m);
L=zeros(m);
for j=1:m
    L(j,j)=1;
end
for j=1:m
    U(1,j)=A(1,j);
end
for i=2:m
    for j=1:m
        for k=1:i-1
            s1=0;
            if k==1
                s1=0;
            else
            for p=1:k-1
                s1=s1+L(i,p)*U(p,k);
            end
            end
            L(i,k)=(A(i,k)-s1)/U(k,k);
           end
         for k=i:m
             s2=0;
           for p=1:i-1
               s2=s2+L(i,p)*U(p,k);
           end
           U(i,k)=A(i,k)-s2;
         end
    end
end
end