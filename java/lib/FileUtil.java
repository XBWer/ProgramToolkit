package ProgrammingToolkit.java.lib;

import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FileUtil {

	public static String[] getSubDirs(String rootDir) {

		File file = new File(rootDir);
		String[] directories = file.list(new FilenameFilter() {
			@Override
			public boolean accept(File current, String name) {
				return new File(current, name).isDirectory();
			}
		});
//		System.out.println(Arrays.toString(directories));
		return directories;
	}

	public static String readFile2Str(String fpath) {
		String content = "";
		try {
			content = new String(Files.readAllBytes(Paths.get(fpath)));
		} catch (IOException e) {
			e.printStackTrace();
		}
		return content;

	}

	public static Boolean writeStr2File(String wStr, String fPath) {
		try {
			Files.write(Paths.get(fPath), wStr.getBytes());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
		return true;
	}

	public static boolean deleteDirectory(File directoryToBeDeleted) {
		File[] allContents = directoryToBeDeleted.listFiles();
		if (allContents != null) {
			for (File file : allContents) {
				deleteDirectory(file);
			}
		}
		return directoryToBeDeleted.delete();
	}

}
