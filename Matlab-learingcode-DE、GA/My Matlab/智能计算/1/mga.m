function g=mga
n=30;
w=30;
up=5;ul=-5;
p=(up-ul)*rand(n,w)+ul
yj=pj(p);
[yj,d]=sort(yj);
p=p(d,:);
    axis([-5,5,-5,5]),plot(p(:,1),p(:,2),'*')
xl=100;xl0=1;
by=0.05;
while xl0<xl
    xl0=xl0+1;
    for i=1:n
    n1=fix(rand*10)+1;
    n2=fix(rand*(n-n1))+n1;
    alf=rand;px(i,:)=alf*p(n1,:)+(1-alf)*p(n2,:);
        if rand<by
            m0=rand(1,w)<0.1;
            sw=fix(rand*w)+1;m0(sw)=logical(1);
            m1=(up-ul)*rand(1,w)+ul;
            m2=px(i,:);m2(sw)=m1(sw);px(i,:)=m2;
        end
    end
    pjx=pj(px);
    pp=[p;px];ppj=[yj;pjx];
    plot(pp(:,1),pp(:,2),'d'),axis([-5,5,-5,5])
    [yj,d]=sort(ppj)
    p=pp(d(1:n),:);
    yj=yj(1:n);
    [p(1:10,:),yj(1:10)]
    plot(p(:,1),p(:,2),'r*'),axis([-5,5,-5,5])
    
    
    
end

function y=pj(x)
y=sum(x.^2,2);
