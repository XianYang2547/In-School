function xianyangt
%320085404113
clc;
clear;
n=50;                                           %��Ⱥ����
w=8;                                            %����ά��
up=50;ul=-50;                                     %������������
p=(up-ul)*rand(n,w)+ul;                         %���ɳ�ʼ��Ⱥ
yj=pj(p);   pjc=n;                              %�Գ�ʼ��Ⱥ���� ��ʼ���۴���
[yj,d]=sort(yj);                                %����ֵ����
p=p(d,:);                                       %����Ⱥ����
xl0=0;                                          %��ʼ������
while xl0<40000 %����������Ϊ5000
    v0=[];%���ɿվ���
    
    for i=1:n
         r=randperm(10);r1=r(1);
         r=randperm(n-r1)+r1;r2=r(1);r3=r(2);
         if r2>r3,x=r2;r2=r3;r3=x;end %����r1r2r3
         v=p(r1,:)+0.4*rand(1,w).*(p(r2,:)-p(r3,:)); %����һ�����ʸ��
         x=(up-ul)*rand(1,w)+ul;%����һ���µĸ���x
         
         x0=v>up|v<ul;%�ж�v��Ԫ���Ƿ�Խ�磬����1��5�е��߼�����
         x1=any(x0);%�ж�x0��ÿһ���Ƿ�Ϊ����Ԫ�� ����0����1
         if rand<0.8||x1%������������滻 rand<0.8����x1Ϊ1
             x2=rand(1,w)<0.2;%����һ���߼�����x2
             x3=fix(rand*w)+1;%����x3��1-5֮�䣩
             x0(x3)=true;
             x4=x0|x2;
             v(x4)=x(x4);%�滻Խ����Ǹ���
         end
         v0=[v0;v];%��v����v0��
     end
          pjx=pj(v0);  %������Ⱥv0����
          pjc=pjc+n;   %�������۴���                      
         pp=[p;v0]; %���¾���Ⱥ����һ��
         ppj=[yj;pjx]; %������ֵ����һ��                        
         [yj,d]=sort(ppj);%����ֵ����
         p=pp(d(1:n),:);  %ȡǰ30������
       
         yj=yj(1:n); %ȡǰ30���� 
         [p([1:5],:),yj(1:5)];%��ʾ��ǰ5������
          if yj(1)<1e-5,break,end %����С��1e-5����ֹͣ
         xl0=xl0+1;%����+1
         if xl0==1
          figure(1)
         axis([-50,50,-50,50]),plot(p(:,1),p(:,2),'*') 
         end
          if xl0==100
          figure(2)
         axis([-50,50,-50,50]),plot(p(:,1),p(:,2),'*') 
         end
end
%%
disp(['bestfi:   ',num2str(p(1,:))])       %��ʾ��õĸ���
disp(['bests:    ',num2str(yj(1))])         %��ʾ��õĽ�
pjc; xl0                                          %���۴���
figure(3)
axis([-50,50,-50,50]),plot(p(:,1),p(:,2),'*') 
end

%% ����
function y=pj(x)                                                   
y=sum(x.^2,2);
end
