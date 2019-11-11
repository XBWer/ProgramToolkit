import java.util.List;

import smu.bowen.epr.utils.FileUtil;

public class DiffUtil {

	public static int getChangedLine(String diffFilePath) {
		List<String> diffFileStrList = FileUtil.readFileToStrList(diffFilePath);
		for (String line : diffFileStrList) {
			if (line.startsWith("@@")) {
				for (String tmp : line.split(" ")) {
					if (tmp.trim().startsWith("-") && !tmp.contains(",")) {
						return Integer.valueOf(tmp.trim().replace("-", ""));
					}
					if (tmp.startsWith("+")) {
						return Integer.valueOf(tmp.trim().replace("+", ""));
					}
				}
			}
		}
		System.out.println(diffFilePath);
		System.exit(0);
		return -1;
	}

}
