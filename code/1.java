import java.io.FileInputStream;  
import java.io.IOException;  
import java.io.InputStream;  
import jxl.Cell;  
import jxl.Sheet;  
import jxl.Workbook;  
import jxl.read.biff.BiffException;  
public class ReadExcel {  
    public static int insertIntoDBFromExcel(String filePath) throws BiffException, IOException {  
    	int flag = 1;//成功返回1
    	try{

    		// 1、构造excel文件输入流对象  
	        String sFilePath = filePath;//比如 "D:/1.xls";  
	        InputStream is = new FileInputStream(sFilePath);  
	        // 2、声明工作簿对象  
	        Workbook rwb = Workbook.getWorkbook(is);  
	        // 3、获得工作簿的个数,对应于一个excel中的工作表个数  
	        rwb.getNumberOfSheets();  
	  
	        Sheet oFirstSheet = rwb.getSheet(0);// 使用索引形式获取第一个工作表，也可以使用rwb.getSheet(sheetName);其中sheetName表示的是工作表的名称  
	//        System.out.println("工作表名称：" + oFirstSheet.getName());  
	        int rows = oFirstSheet.getRows();//获取工作表中的总行数  
	        int columns = oFirstSheet.getColumns();//获取工作表中的总列数  
	        for (int i = 0; i < rows; i++) {  
	            for (int j = 0; j < columns; j++) {  
	                Cell oCell= oFirstSheet.getCell(j,i);//需要注意的是这里的getCell方法的参数，第一个是指定第几列，第二个参数才是指定第几行  
	                System.out.println(oCell.getContents()+"\r\n");  
	                //从oCell中读取数据，拼装成User放入list
	            }  
	        }  
	        //调用JDBCUtil插入list
    	}catch(Exception e){
    		flag = 0;//失败返回0
    	}
        return 0;
    }  
  
}  