function tsp
clc;clear all;
load mydata
A=dt50;
%B=fliplr(A);
C=A';
%C=rot90(B);
N=size(C,1);%TSP问题的规模，即城市数目
D=zeros(N);%任意两个城市距离间隔矩阵
%求任意两个城市距离间隔矩阵
for i=1:N
    for j=1:N
        D(i,j)=((C(i,1)-C(j,1))^2+(C(i,2)-C(j,2))^2)^0.5;
    end
end
NP=200;%免疫个体数目
G=3000;%最大免疫代数
f=zeros(N,NP);%用于存储种群   30*200
for i=1:NP
    f(:,i)=randperm(N)';%随机生成初始种群  
end

for i=1:NP
    len(i)=func3(D,f(:,i),N);%计算路径长度
end
[Sortlen,Index]=sort(len);
Sortf=f(:,Index);%种群个体排序
R = Sortf(:,1);%存储最优个体
len=zeros(NP,1);%存储路径长度
gen=1;%免疫代数
Ncl=10;%克隆个数
%免疫循环
while gen < G
    for i=1:NP/2 %选激励度前NP/2个个体进行免疫操作
        a=Sortf(:,i);
        Ca=repmat(a,1,Ncl);
        for j=2:Ncl   %保留克隆源
            p1=floor(1+N*rand);
            p2=floor(1+N*rand);
            while p1==p2
                p1=floor(1+N*rand);
                p2=floor(1+N*rand);
            end
           tmp=Ca(p1,j);
            Ca(p1,j)=Ca(p2,j);
            Ca(p2,j)=tmp;
        end
      % Ca(:,1)=Sortf(:,i);%保留克隆源
        %克隆抑制保留亲和度最高的个体
        for j=1:Ncl
            Calen(j)=func3(D,Ca(:,j),N);
        end
        [SortCalen,Index]=sort(Calen);
        %SortCa=Ca(:,Index);
        af(:,i)=Ca(:,Index(1));%af(:,i)=SortCa(:,1);
        alen(i)=SortCalen(1);
    end
   
    
    for i=1:NP/2
    sn1=fix(rand*100+1);    sn2=fix(rand*100+1); 
    while sn1==sn2
      sn1=fix(rand*100+1);    sn2=fix(rand*100+1);           
    end
    s1=af(:,sn1);s10=s1;     s2=af(:,sn2);s20=s2;
     
     rL=fix(rand*4+2);
     r1w=fix(rand*(30-rL)+1);
     s0=s1(r1w:(r1w+rL-1));
    for i=1:rL
    s=s0(i);
    t1=find(s2==s);
    s2(t1)=[];
    end
    %r1w=fix(rand*(30-rL)+1);
    s2=[s2(1:(r1w-1));s0;s2(r1w:end)];
    slen2=func3(D,s2,N);

     
    s0=s20(r1w:(r1w+rL-1));
    for i=1:rL
    s=s0(i);
    t1=find(s1==s);
    s1(t1)=[];
    end
    %r1w=fix(rand*(30-rL)+1);
    s1=[s1(1:(r1w-1));s0;s1(r1w:end)];
    slen1=func3(D,s1,N);

    slen10=func3(D,s10,N);    slen20=func3(D,s20,N);
    if min([slen1 slen2])<min([slen10 slen20])
        af(:,sn1)=s1;af(:,sn2)=s2;alen(sn1)=slen1;alen(sn2)=slen2;
    end
end
    
 %种群刷新
    for i=1:NP/2
        bf(:,i)=randperm(N)';%随机生成初始种群
        blen(i)=func3(D,bf(:,i),N);%计算路径长度
    end
    %免疫种群与新种群合并
    f=[af,bf];
    len=[alen,blen];
    [Sortlen,Index]=sort(len);
    Sortf=f(:,Index);
    
    
    
    %[Sortslen,Index]=sort(slen);
    %Sortsf=f(:,Index);
    gen=gen+1;
    trace(gen)=Sortlen(1);
    if gen/100==fix(gen/100)
   gen, Bestf= [Sortf(:,1:5)]',Sortlen(1:5)
   Bestlen=trace(end)
    end
end
%输出优化结果
Bestf=Sortf(:,1)'%最优变量
Bestlen=trace(end)
figure
for i=1:N-1
    plot([C(Bestf(i),1),C(Bestf(i+1),1)],...
        [C(Bestf(i),2),C(Bestf(i+1),2)],'bo-');
    hold on;
end
  plot([C(Bestf(N),1),C(Bestf(1),1)],...
        [C(Bestf(N),2),C(Bestf(1),2)],'ro-');
    
    title(['优化最优距离：',num2str(trace(end))]);
   figure,plot(trace)
    xlabel('迭代次数')
    ylabel('目标函数值')
    title('亲和度进化曲线')
    %计算路线总长度

function len=func3(D,f,N)
    len =D(f(N),f(1));
    for i=1:(N-1)
        len=len+D(f(i),f(i+1));
    end
