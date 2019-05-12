#include <vector>
#include <string>

namespace VericStrong
{
	std::string dumps(const std::vector<std::string> &obj);

	std::vector<std::string> loads(const std::string &dump);
}