function Drawfunc(label)

x=-5:0.05:5;%41列的向量
if label==1
    y = x;
    [X,Y] = meshgrid(x,y);
    [row,col] = size(X);
    for  l = 1 :col
         for  h = 1 :row
            z(h,l) = Rastrigin([X(h,l),Y(h,l)]);
        end
    end
    surf(X,Y,z);
    shading interp
    xlabel('x1-axis'),ylabel('x2-axis'),zlabel('f-axis'); 
    title('mesh'); 
end

if label==2
    y = x;
    [X,Y] = meshgrid(x,y);
    [row,col] = size(X);
    for  l = 1 :col
         for  h = 1 :row
            z(h,l) = Schaffer([X(h,l),Y(h,l)]);
        end
    end
    surf(X,Y,z);
    shading interp 
    xlabel('x1-axis'),ylabel('x2-axis'),zlabel('f-axis'); 
    title('mesh'); 
end

if label==3
    y = x;
    [X,Y] = meshgrid(x,y);
    [row,col] = size(X);
    for  l = 1 :col
         for  h = 1 :row
            z(h,l) = Griewank([X(h,l),Y(h,l)]);
        end
    end
    surf(X,Y,z);
    shading interp 
    xlabel('x1-axis'),ylabel('x2-axis'),zlabel('f-axis'); 
    title('mesh'); 
end
  
