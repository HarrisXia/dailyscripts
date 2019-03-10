function [ object,object_num] = read_xml( root,name )

%% Author Danyang Huang
%      2017.7.1
% this function can read xml file
% output object is objects contained in the xml label
%               object_num is the number of the bbox


    
    fid=fopen([root,'/',name]);
    json=fscanf(fid,'%c');
    fclose(fid);
    
        start_postion=strfind(json,'<object>');
        end_position=strfind(json,'</object>');
    

        

        num_object = length(start_postion);    % num of obect

        
       
                    start_postion_xmin=strfind(json,'<xmin>');
                    end_position_xmin=strfind(json,'</xmin>');
                   start_postion_ymin=strfind(json,'<ymin>');
                    end_position_ymin=strfind(json,'</ymin>');
                    start_postion_xmax=strfind(json,'<xmax>');
                    end_position_xmax=strfind(json,'</xmax>');
                    start_postion_ymax=strfind(json,'<ymax>');
                    end_position_ymax=strfind(json,'</ymax>');
                    start_position_name=strfind(json(start_postion:end),'<name>');
                    end_position_name=strfind(json(start_postion:end),'</name>');
        
          
        boxes=[];
        names=[];
      
         for  mm=1:  length(start_postion_xmin) 
                 k=end_position_xmin(mm)-start_postion_xmin(mm);
             xmin= str2num(json((end_position_xmin(mm)-(k-6)):end_position_xmin(mm)-1));
                 k=end_position_ymin(mm)-start_postion_ymin(mm);
              ymin=str2num(json((end_position_ymin(mm)-(k-6)):end_position_ymin(mm)-1));
                 k=end_position_xmax(mm)-start_postion_xmax(mm);
              xmax=str2num(json((end_position_xmax(mm)-(k-6)):end_position_xmax(mm)-1));
                  k=end_position_ymax(mm)-start_postion_ymax(mm);
              ymax=str2num(json((end_position_ymax(mm)-(k-6)):end_position_ymax(mm)-1));
                  k=end_position_name(mm)-start_position_name(mm);
                  json_object=json(start_postion:end);
              name=json_object((end_position_name(mm)-(k-6)):end_position_name(mm)-1);
              
%               names={names;name};
              names{mm}=name;
              box=[xmin,ymin,xmax,ymax];
              boxes=[boxes;
                              box];
               w=(xmax- xmin);     
               h=(ymax-ymin);
          %  rectangle('Position', [xmin, ymin, w, h], 'LineWidth',2, 'EdgeColor', 'blue');  
                       
         end  
        [m,n]=size(boxes);
        numboxes=m;

         
         for i=1:numboxes
             object(i).box=boxes(i,:);
             object(i).name=names{i};
         end
         object_num=m;
end

