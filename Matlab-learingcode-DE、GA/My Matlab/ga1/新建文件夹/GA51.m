
tic
p=[];
for i=1:200
z=fix(rand(1,35)*10);    
strn=num2str(z);
strn=strn(1:3:103);
p=[p;strn];

x1=(p(i,:));
x2=jma(x1);                    %解码
pj(i)=sum(((x2)-(1:5)).^2);
end
[Oderfi,Indexfi]=sort(pj);
Bestfi=Oderfi(1);            %取当前最小值
BestS=p(Indexfi(1),:);       %最小值对应的染色体
p=p(Indexfi,:);
pj=pj(Indexfi);
[[jma(p(1,:));jma(p(2,:));jma(p(3,:));jma(p(4,:));jma(p(5,:));],[pj(1:5)]'];

%交叉
for e=1:1000              
for b=1:50
x3=ceil(50*rand);x4=ceil(100*rand);
while x3==x4,x4=ceil(100*rand);end
y1=p(x3,:);y2=p(x4,:);
w=rand(1,35)<0.4;
y11=y1(w);y21=y2(w);
y2(w)=y11;y1(w)=y21;

%变异
if rand<0.1
  z=fix(rand(1,35)*10); strn=num2str(z);strn=strn(1:3:103);
  byw=rand(1,35)<0.1;
  y11=strn(byw);  y2(byw)=y11;
  z=fix(rand(1,35)*10); strn=num2str(z);strn=strn(1:3:103);
  byw=rand(1,35)<0.05;
  y11=strn(byw);  y1(byw)=y11;
end
  
%评价选择
x2=jma(y1); %解码
pj1=sum(((x2)-(1:5)).^2);
x2=jma(y2); %解码
pj2=sum(((x2)-(1:5)).^2);
if min(pj1,pj2)<min(pj([x3,x4]))
    p(x3,:)=y1;pj(x3)=pj1;
    p(x4,:)=y2;pj(x4)=pj2;
end

end 

[Oderfi,Indexfi]=sort(pj);
Bestfi=Oderfi(1);            %取当前最小值
BestS=p(Indexfi(1),:);       %最小值对应的染色体
p=p(Indexfi,:);
pj=pj(Indexfi);
if e/10==fix(e/10)
[ [jma(p(1,:));jma(p(2,:));jma(p(3,:));jma(p(4,:));jma(p(5,:));],[pj(1:5)]'];
p(1:5,:);
 e
Bestfi,BestS
end

end 
toc



